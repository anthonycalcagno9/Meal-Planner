from fastapi import FastAPI
from api import health, generateMealPlan

app = FastAPI(
    title="Meal Planner API",
    description="A FastAPI application for managing weekly meal plans",
    version="0.1.0"
)

# Include routers
app.include_router(health.router)
app.include_router(generateMealPlan.router)


@app.get("/")
async def root():
    """Welcome endpoint for the Meal Planner API."""
    return {
        "message": "Welcome to the Meal Planner API!",
        "docs": "/docs",
        "health": "/health"
    }

