from pydantic import BaseModel, HttpUrl

class CreateShortUrlRequest(BaseModel):
    original_url: HttpUrl

class CreateShortUrlResponse(BaseModel):
    short_code: str