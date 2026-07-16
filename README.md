# URL Shortener API

A backend API for generating short codes for URLs and redirecting users to the original address.

This project is being built as a portfolio application focused on clean backend practices, validation, testing, containerization, and CI/CD.

## Tech stack

- Python 3.13
- FastAPI
- Pydantic
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

## API endpoints

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

### Create a short URL code

```http
POST /urls
```

Request body:

```json
{
  "original_url": "https://www.example.com"
}
```

Response — `201 Created`:

```json
{
  "short_code": "aB3k9x"
}
```

The API validates the submitted URL and returns `422 Unprocessable Content` for invalid input.

### Redirect to the original URL

```http
GET /{short_code}
```

Example:

```text
http://127.0.0.1:8000/aB3k9x
```

If the code exists, the API returns a `307 Temporary Redirect` to the original URL. If it does not exist, the API returns `404 Not Found`.

## API documentation

FastAPI automatically generates interactive documentation:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Current limitations

URLs are currently stored in memory, so all generated codes are lost when the application restarts.

## Planned improvements

- Persistent storage with PostgreSQL
- Automated tests with pytest
- Docker and Docker Compose
- CI/CD with GitHub Actions
- Custom aliases and URL expiration dates
- Click analytics