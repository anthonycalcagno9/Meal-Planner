from typing import Optional, Dict, Any


class MealData:
    """Represents a single meal with description, website link, and ingredients."""
    
    def __init__(self, description: Optional[str] = None, website: Optional[str] = None, ingredients: Optional[Dict[str, str]] = None):
        self.description = description
        self.website = website
        self.ingredients = ingredients or {}
    
    def __str__(self):
        return f"{self.description}" + (f" (Link: {self.website})" if self.website else "")
    
    def __repr__(self):
        return f"MealData(description='{self.description}', website='{self.website}', ingredients={self.ingredients})"


class DayOfMeals:
    """Represents meals for a single day with breakfast, lunch, and dinner."""
    
    def __init__(self, breakfast: Optional[MealData] = None, lunch: Optional[MealData] = None, dinner: Optional[MealData] = None):
        self.breakfast = breakfast or MealData()
        self.lunch = lunch or MealData()
        self.dinner = dinner or MealData()
    
    def __str__(self):
        return f"Breakfast: {self.breakfast}, Lunch: {self.lunch}, Dinner: {self.dinner}"
    
    def __repr__(self):
        return f"DayOfMeals(breakfast={self.breakfast!r}, lunch={self.lunch!r}, dinner={self.dinner!r})"


class WeekOfMeals:
    """Represents a week's worth of meals from Monday to Sunday."""
    
    def __init__(self):
        self.monday = DayOfMeals()
        self.tuesday = DayOfMeals()
        self.wednesday = DayOfMeals()
        self.thursday = DayOfMeals()
        self.friday = DayOfMeals()
        self.saturday = DayOfMeals()
        self.sunday = DayOfMeals()
    
    def __str__(self):
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        result = "Week of Meals:\n"
        for day in days:
            day_attr = day.lower()
            day_meals = getattr(self, day_attr)
            result += f"{day}: {day_meals}\n"
        return result
    
    def __repr__(self):
        return "WeekOfMeals()"
