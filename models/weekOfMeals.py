from typing import Optional, List
from pydantic import BaseModel, Field

class IngredientData(BaseModel):
    """Represents an ingredient with its name and quantity."""
    
    name: str
    quantity: str  # e.g., "2 cups", "1 tablespoon", etc.
    
class MealData(BaseModel):
    """Represents a single meal with description, website link, and ingredients."""
    
    description: Optional[str] = None
    website: Optional[str] = None
    ingredients: Optional[List[IngredientData]] = None


class DayOfMeals(BaseModel):
    """Represents meals for a single day with breakfast, lunch, and dinner."""
    
    breakfast: MealData = Field(default_factory=MealData)
    lunch: MealData = Field(default_factory=MealData)
    dinner: MealData = Field(default_factory=MealData)
    

class WeekOfMeals(BaseModel):
    """Represents a week's worth of meals from Monday to Sunday."""
    
    monday: DayOfMeals = Field(default_factory=DayOfMeals)
    tuesday: DayOfMeals = Field(default_factory=DayOfMeals)
    wednesday: DayOfMeals = Field(default_factory=DayOfMeals)
    thursday: DayOfMeals = Field(default_factory=DayOfMeals)
    #friday: DayOfMeals = Field(default_factory=DayOfMeals)
    #saturday: DayOfMeals = Field(default_factory=DayOfMeals)
    #sunday: DayOfMeals = Field(default_factory=DayOfMeals)


class SimpleJsonMeals(BaseModel):
    """Represents a simple JSON structure for meals."""
    
    breakfast: str
    lunch: str
    dinner: str


