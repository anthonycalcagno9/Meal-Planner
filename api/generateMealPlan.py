from urllib import response
from fastapi import APIRouter, HTTPException
from typing import Optional, List
from models.weekOfMeals import WeekOfMeals, DayOfMeals, MealData, SimpleJsonMeals
from pydantic import BaseModel
import json
import openai
import os

router = APIRouter(prefix="/meal-plan", tags=["meal-planning"])

# Request model for the meal plan generation
class MealPlanRequest(BaseModel):
    disliked_foods: List[str] = []
    prompt: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "disliked_foods": ["mushrooms", "spinach", "fish"],
                "prompt": "Create a healthy meal plan focused on Mediterranean cuisine with lots of vegetables"
            }
        }


@router.post("/generate-meal-plan", summary="Generate a weekly meal plan")
async def generate_meal_plan(request: MealPlanRequest):
    """
    Generate a weekly meal plan using OpenAI's LLM based on user preferences.
    
    Args:
        request: MealPlanRequest containing:
            - disliked_foods: List of foods the user doesn't like
            - prompt: User's custom prompt for meal planning
    
    Returns:
        WeekOfMeals: A complete week of AI-generated meals
    """
    try:
        # Check for OpenAI API key
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            raise HTTPException(
                status_code=500, 
                detail="OpenAI API key not configured. Please set OPENAI_API_KEY environment variable."
            )
        
        # Set up OpenAI client
        client = openai.OpenAI(api_key=openai_api_key)
        
        # Create the system prompt
        system_prompt = """You are a professional meal planning assistant. Generate a weekly meal plan based on user preferences.
        
        Create varied, balanced, and nutritious meals for each day of the week.
        Each meal should include:
        - A clear, appetizing meal name
        - A realistic recipe URL (you can search for actual recipes online)
        - Ingredients with proper quantities and units (cups, tablespoons, ounces, etc.)
        
        Use web search to find current, popular, and highly-rated recipes that match the user's preferences.
        Make sure to avoid any foods the user has specified they don't like."""
        
        # Create the user prompt with restrictions
        disliked_foods_text = ", ".join(request.disliked_foods) if request.disliked_foods else "none specified"
        
        user_prompt = f"""
        User request: {request.prompt}
        
        Foods to avoid: {disliked_foods_text}
        
        Please create a weekly meal plan that follows the user's request while avoiding the specified foods.
        Use web search to find actual recipe URLs and ensure the meals are current and popular.
        """
        
        # Call OpenAI Responses API with tools and structured output
        if True:
            response = client.responses.parse(
                model="gpt-4.1-mini",  # Using gpt-4o for better responses API support
                input=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                tools=[{ "type": "web_search_preview" }],
                text_format=WeekOfMeals
            )
        else:
            print("MOCKING")
            response = None
        # Parse the response - it should already be structured
        print("====================")
        print(response)
        print("====================")
        print("***********************")
        print("Type of response.output_parsed:", type(response.output_parsed))
        print("Value of response.output_parsed:", response.output_parsed)
        print("***********************")

        # Get token usage and calculate cost
        usage = response.usage
        input_tokens = usage.input_tokens
        output_tokens = usage.output_tokens
        total_tokens = usage.total_tokens

        # GPT-4o pricing (as of 2024)
        # Input: $0.0025 per 1K tokens
        # Output: $0.01 per 1K tokens
        input_cost = (input_tokens / 1000) * 0.0025
        output_cost = (output_tokens / 1000) * 0.01
        total_cost = input_cost + output_cost

        print(f"🔢 Token Usage:")
        print(f"   Input tokens: {input_tokens}")
        print(f"   Output tokens: {output_tokens}")
        print(f"   Total tokens: {total_tokens}")
        print(f"💰 Cost Breakdown:")
        print(f"   Input cost: ${input_cost:.6f}")
        print(f"   Output cost: ${output_cost:.6f}")
        print(f"   Total cost: ${total_cost:.6f}")

        return {
            "message": "AI-generated meal plan created successfully!",
            "usage": {
                "input_tokens": input_tokens,
                "output_tokens": output_tokens,
                "total_tokens": total_tokens
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
