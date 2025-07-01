from typing import Optional
from pydantic import BaseModel, Field


class I(BaseModel):
    """Represents an ingredient with its name and quantity."""
    n: str
    q: str


class M(BaseModel):
    """Represents a single meal with description and link."""
    d: Optional[str] = None
    l: Optional[str] = None

class D(BaseModel):
    """Represents meals for a single day with breakfast, lunch, and dinner."""
    b: M = Field(default_factory=M)
    l: M = Field(default_factory=M)
    d: M = Field(default_factory=M)


class W(BaseModel):
    """Represents a week's worth of meals from Monday to Sunday."""
    m: D = Field(default_factory=D)   # Monday
    #t: D = Field(default_factory=D)   # Tuesday
    #w: D = Field(default_factory=D)   # Wednesday
    #th: D = Field(default_factory=D)  # Thursday
    #f: D = Field(default_factory=D)   # Friday
    #s: D = Field(default_factory=D)   # Saturday
    #su: D = Field(default_factory=D)  # Sunday



