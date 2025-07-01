from fastapi import APIRouter
from datetime import datetime

router = APIRouter(prefix="/health", tags=["health"])


@router.get("/")
async def health_check():
    """Health check endpoint to verify the API is running."""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "meal-planner"
    }
