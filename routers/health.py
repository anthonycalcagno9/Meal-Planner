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


@router.get("/detailed")
async def detailed_health_check():
    """Detailed health check with more information."""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "meal-planner",
        "version": "0.1.0",
        "uptime": "running",
        "dependencies": {
            "database": "not configured",
            "external_apis": "not configured"
        }
    }
