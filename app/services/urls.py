import secrets
import string

urls_dict: dict[str, str] = {}

def create_short_code(url: str) -> str:
    alphabet = string.ascii_letters + string.digits
    short_code = "".join(secrets.choice(alphabet) for i in range(6))

    while short_code in urls_dict:
        alphabet = string.ascii_letters + string.digits
        short_code = "".join(secrets.choice(alphabet) for i in range(6))

    urls_dict[short_code] = url

    return short_code

def get_original_url(short_code: str) -> str | None:
    return urls_dict.get(short_code)