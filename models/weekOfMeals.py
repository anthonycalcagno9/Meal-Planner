from typing import Optional, List
from pydantic import BaseModel, Field

# IngredientData class to represent an ingredient with its name and quantity
#Using I because that helps keep output shorter for LLMs
class I(BaseModel):
    """Represents an ingredient with its name and quantity."""
    
    n: str
    q: str  # e.g., "2 cups", "1 tablespoon", etc.
    
#MealData class, shortening to M for brevity in LLM outputs
class M(BaseModel):
    """Represents a single meal with description, website link, and ingredients."""
    
    d: Optional[str] = None
    l: Optional[str] = None


#DayOfMeals = D so output is shorter for LLMs
class D(BaseModel):
    """Represents meals for a single day with breakfast, lunch, and dinner."""

    b: M = Field(default_factory=M)
    l: M = Field(default_factory=M)
    d: M = Field(default_factory=M)


#WeekOfMeals = W so output is shorter for LLMs
class W(BaseModel):
    """Represents a week's worth of meals from Monday to Sunday."""

    m: D = Field(default_factory=D)
    #t: D = Field(default_factory=D)
    #w: D = Field(default_factory=D)
    #th: D = Field(default_factory=D)
    #f: D = Field(default_factory=D)
    #s: D = Field(default_factory=D)
    #su: D = Field(default_factory=D)



