from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import secrets
import string

from app.schemas import CreateShortUrlRequest, CreateShortUrlResponse

app = FastAPI()

urls_dict = {}

def create_short_code(url: str) -> str:
    alphabet = string.ascii_letters + string.digits
    short_code = "".join(secrets.choice(alphabet) for i in range(6))

    while short_code in urls_dict:
        alphabet = string.ascii_letters + string.digits
        short_code = "".join(secrets.choice(alphabet) for i in range(6))

    urls_dict[short_code] = url

    return short_code

@app.get("/health", status_code=200)
def check_health():
    return {"status": "ok"}

@app.post("/urls", status_code=201)
def get_shot_url(payload: CreateShortUrlRequest) -> CreateShortUrlResponse:
    short_code = create_short_code(str(payload.original_url))

    return CreateShortUrlResponse(short_code=short_code)

@app.get("/{short_code}")
def redirect_to_original_url(short_code: str) -> RedirectResponse:
    original_url = urls_dict.get(short_code)

    if original_url is None:
        raise HTTPException(status_code=404, detail="Short URL not found")

    return RedirectResponse(url=original_url, status_code=307)