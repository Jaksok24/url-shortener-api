# URL Shortener API

A backend API for creating and managing shortened URLs.  
This project is being built as a portfolio application with a focus on clean backend practices, testing, containerization, and CI/CD.

## Tech stack

- Python 3.13
- FastAPI
- Uvicorn

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/Jaksok24/url-shortener-api.git
cd url-shortener-api
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## Available endpoints

### Health check

```http
GET /health
```

Response:

```json
{
  "status": "ok"
}
```

## API documentation

FastAPI automatically generates interactive API documentation:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Project status

In progress. The first implemented feature is the health-check endpoint.

Planned next steps include URL creation, redirects, persistent storage, automated tests, Docker, and CI/CD.