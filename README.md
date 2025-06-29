# Meal Planner API

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green.svg)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A modern FastAPI application for managing weekly meal plans and generating grocery lists. Plan your meals for the week, track ingredients, and streamline your cooking routine.

## 🚀 Features

- **Weekly Meal Planning**: Organize breakfast, lunch, and dinner for each day of the week
- **Recipe Management**: Store meal descriptions with links to recipes
- **Ingredient Tracking**: Track ingredients with quantities for each meal
- **RESTful API**: Full CRUD operations via FastAPI
- **Interactive Documentation**: Automatic API docs with Swagger UI
- **Health Monitoring**: Built-in health check endpoints
- **Data Models**: Structured meal data with proper validation

## 📋 Table of Contents

- [Features](#-features)
- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Usage](#-usage)
- [API Documentation](#-api-documentation)
- [Data Models](#-data-models)
- [Development](#-development)
- [Testing](#-testing)
- [Deployment](#-deployment)
- [Contributing](#-contributing)
- [License](#-license)

## 🚀 Quick Start

```bash
# Clone the repository
git clone <repository-url>
cd meal-planner

# Install dependencies
uv sync

# Run the application
uv run python run.py
```

The API will be available at `http://localhost:8000`

## 📦 Installation

### Prerequisites

- Python 3.13 or higher
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

### Option 1: Using uv (Recommended)

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync

# Activate virtual environment (optional)
source .venv/bin/activate
```

### Option 2: Using pip

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## 🎯 Usage

### Starting the Server

```bash
# Method 1: Using run.py (recommended)
uv run python run.py

# Method 2: Using uvicorn directly
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Method 3: Using the start script
./start.sh
```

### Making API Requests

```bash
# Check health
curl http://localhost:8000/health/

# Get welcome message
curl http://localhost:8000/

# View interactive docs
open http://localhost:8000/docs
```

## 📚 API Documentation

Once the server is running, you can access:

- **Swagger UI**: `http://localhost:8000/docs` - Interactive API documentation
- **ReDoc**: `http://localhost:8000/redoc` - Alternative documentation format
- **OpenAPI Schema**: `http://localhost:8000/openapi.json` - Raw OpenAPI specification

### Available Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Welcome message and API info |
| `GET` | `/health/` | Basic health check |
| `GET` | `/health/detailed` | Detailed health information |
| `GET` | `/docs` | Interactive API documentation |

## 🏗️ Data Models

### MealData
Represents a single meal with description, recipe link, and ingredients.

```python
{
    "description": "Oatmeal with berries and honey",
    "website": "https://example.com/recipe",
    "ingredients": {
        "rolled oats": "0.5 cups",
        "mixed berries": "0.25 cups",
        "honey": "2 tablespoons"
    }
}
```

### DayOfMeals
Contains three meals for a single day.

```python
{
    "breakfast": MealData,
    "lunch": MealData,
    "dinner": MealData
}
```

### WeekOfMeals
Represents a complete week of meal planning.

```python
{
    "monday": DayOfMeals,
    "tuesday": DayOfMeals,
    "wednesday": DayOfMeals,
    # ... etc
}
```

## 🛠️ Development

### Project Structure

```
meal-planner/
├── main.py              # FastAPI application entry point
├── run.py               # Development server runner
├── start.sh             # Quick start script
├── models/              # Data models
│   └── weekOfMeals.py   # Meal planning models
├── routers/             # API route handlers
│   └── health.py        # Health check endpoints
├── pyproject.toml       # Project configuration
├── uv.lock             # Dependency lock file
└── README.md           # This file
```

### Code Style

This project uses:
- **Ruff**: For linting and code formatting
- **Type hints**: For better code documentation and IDE support
- **Async/await**: For FastAPI best practices

### Running with Hot Reload

```bash
# Auto-restart on file changes
uv run python run.py
```

## 🧪 Testing

```bash
# Run health check test
curl -f http://localhost:8000/health/ || echo "Health check failed"

# Test all endpoints
curl http://localhost:8000/
curl http://localhost:8000/health/
curl http://localhost:8000/health/detailed
```

## 🚀 Deployment

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `HOST` | Server host | `0.0.0.0` |
| `PORT` | Server port | `8000` |
| `LOG_LEVEL` | Logging level | `info` |

### Docker (Coming Soon)

```dockerfile
# Dockerfile example
FROM python:3.13-slim
WORKDIR /app
COPY . .
RUN pip install uv && uv sync
CMD ["uv", "run", "python", "run.py"]
```

### Production Considerations

- Use a production ASGI server like Gunicorn with Uvicorn workers
- Set up proper logging and monitoring
- Configure environment-specific settings
- Implement authentication and authorization
- Add rate limiting and security headers

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Install development dependencies
uv sync --dev

# Run linting
uv run ruff check .

# Format code
uv run ruff format .
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - The web framework used
- [Uvicorn](https://www.uvicorn.org/) - ASGI server implementation
- [uv](https://github.com/astral-sh/uv) - Fast Python package installer

## 📞 Support

If you have any questions or need help:

1. Check the [API documentation](http://localhost:8000/docs)
2. Review existing [issues](https://github.com/your-repo/issues)
3. Create a new issue with detailed information

---

**Happy meal planning! 🍽️**
