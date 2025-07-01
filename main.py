from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import health, generateMealPlan

app = FastAPI(
    title="Meal Planner API",
    description="A FastAPI application for generating weekly meal plans",
    version="0.1.0"
)

# Include routers
app.include_router(health.router)
app.include_router(generateMealPlan.router)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Welcome endpoint for the Meal Planner API."""
    return {
        "message": "Welcome to the Meal Planner API!",
        "docs": "/docs",
        "health": "/health"
    }

