# Meal Planner API

A FastAPI-based application that generates weekly meal plans using OpenAI's LLM.

## Project Structure

```
meal-planner/
├── app/
│   ├── api/          # API endpoints
│   ├── models/       # Pydantic data models
│   ├── tests/        # Test data and mocks
│   └── core/         # Core utilities (future use)
├── main.py           # FastAPI application
├── run.py            # Development server
└── pyproject.toml    # Project dependencies
```

## Features

- Generate weekly meal plans with OpenAI integration
- Avoid specified disliked foods
- Automatic fallback to mock data when API key not available
- Token usage and cost calculation
- Clean, professional API structure

## Quick Start

1. Install dependencies: `uv sync`
2. (Optional) Set OpenAI API key: `export OPENAI_API_KEY=your_key`
3. Run the server: `uv run python run.py`
4. Visit: `http://localhost:8000/docs`

## API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check
- `POST /meal-plan/generate-meal-plan` - Generate meal plan
