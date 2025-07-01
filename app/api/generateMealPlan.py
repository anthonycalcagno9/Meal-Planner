from fastapi import APIRouter, HTTPException
from typing import List
from app.models.weekOfMeals import W
from app.models.mockOpenAiResponse import MockOpenAIResponse, Usage
from app.tests.mock import mock_output_parsed_1_day
from pydantic import BaseModel
import openai
import os

router = APIRouter(prefix="/meal-plan", tags=["meal-planning"])


class MealPlanRequest(BaseModel):
    disliked_foods: List[str] = []
    prompt: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "disliked_foods": ["mushrooms", "spinach", "fish"],
                "prompt": "Create a healthy meal plan focused on low-carb options"
            }
        }


@router.post("/generate-meal-plan", summary="Generate a weekly meal plan")
async def generate_meal_plan(request: MealPlanRequest):
    """
    Generate a weekly meal plan using OpenAI's LLM based on user preferences.
    
    Args:
        request: MealPlanRequest containing disliked foods and prompt
    
    Returns:
        WeekOfMeals: A complete week of AI-generated meals
    """
    try:
        # Check for OpenAI API key
        openai_api_key = os.getenv("OPENAI_API_KEY")
        use_mock = not openai_api_key
        
        if use_mock:
            # Use mock response
            mock_usage = Usage(input_tokens=100, output_tokens=50, total_tokens=150)
            response = MockOpenAIResponse(output_parsed=mock_output_parsed_1_day, usage=mock_usage)
        else:
            # Use real OpenAI API
            client = openai.OpenAI(api_key=openai_api_key)
            
            system_prompt = """You are a professional meal planning assistant. Generate a weekly meal plan based on user preferences.
            
            Create varied, balanced, and nutritious meals for each day of the week.
            Each meal should include a short and clear meal name. A real recipe URL.
            Use web search to find current real recipes that match the user's preferences and that's the url you should return to the user.
            You need to ensure that the links work and that a user can take that link and find the recipe.
            Also, you can only use recipes that feature one specific dish. 
            You cannot use the same recipe more than once.
            The most important thing is to guarantee that you are returning valid urls that don't result in 404 errors or cannot be found errors.
            Make sure to avoid any foods the user has specified they don't like."""

            disliked_foods_text = ", ".join(request.disliked_foods) if request.disliked_foods else "none specified"
            user_prompt = f"""
            User request: {request.prompt}
            Foods to avoid: {disliked_foods_text}
            
            Please create a weekly meal plan that follows the user's request while avoiding the specified foods.
            Use web search to find actual recipe URLs and ensure the meals are current and popular.
            """
            
            response = client.responses.parse(
                model="gpt-4o",
                input=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                tools=[{"type": "web_search_preview"}],
                text_format=W
            )

        # Calculate cost (GPT-4o pricing)
        usage = response.usage
        input_cost = (usage.input_tokens / 1000) * 0.0025
        output_cost = (usage.output_tokens / 1000) * 0.01
        total_cost = input_cost + output_cost

        return {
            "message": "Meal plan generated successfully!",
            "week_of_meals": response.output_parsed,
            "usage": {
                "input_tokens": usage.input_tokens,
                "output_tokens": usage.output_tokens,
                "total_tokens": usage.total_tokens
            },
            "cost": {
                "input_cost": round(input_cost, 6),
                "output_cost": round(output_cost, 6),
                "total_cost": round(total_cost, 6),
                "currency": "USD"
            }
        }
    
    except openai.OpenAIError as e:
        raise HTTPException(status_code=500, detail=f"OpenAI API error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating meal plan: {str(e)}")
