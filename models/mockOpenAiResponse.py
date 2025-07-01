from pydantic import BaseModel, Field
from typing import TypeVar, Generic, Any, Optional
from models.weekOfMeals import W
# from mocks.mocks import llm_returns_output_parsed


# Generic type for the parsed output (e.g., WeekOfMeals, etc.)
T = TypeVar('T')

class Usage(BaseModel):
    """Represents token usage information from OpenAI API."""
    
    input_tokens: int = Field(description="Number of tokens in the input")
    output_tokens: int = Field(description="Number of tokens in the output") 
    total_tokens: int = Field(description="Total number of tokens used")


class MockOpenAIResponse(BaseModel, Generic[T]):
    """Mock OpenAI response that mimics the structure of responses.parse() output."""
    
    output_parsed: T = Field(description="The parsed response object")
    usage: Usage = Field(description="Token usage information")
    output_parsed = Field(default_factory=W)
    
    class Config:
        arbitrary_types_allowed = True

