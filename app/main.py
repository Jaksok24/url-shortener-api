from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

from app.schemas import CreateShortUrlRequest, CreateShortUrlResponse
from app.services.urls import create_short_code, get_original_url
from app.database import Base, engine

app = FastAPI()

Base.metadata.create_all(engine)

@app.get("/health", status_code=200)
def check_health():
    return {"status": "ok"}

@app.post("/urls", status_code=201)
def get_shot_url(payload: CreateShortUrlRequest) -> CreateShortUrlResponse:
    short_code = create_short_code(str(payload.original_url))

    return CreateShortUrlResponse(short_code=short_code)

@app.get("/{short_code}")
def redirect_to_original_url(short_code: str) -> RedirectResponse:
    original_url = get_original_url(short_code)

    if original_url is None:
        raise HTTPException(status_code=404, detail="Short URL not found")

    return RedirectResponse(url=original_url, status_code=307)