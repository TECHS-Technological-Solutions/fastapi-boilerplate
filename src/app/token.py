import uuid
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from app import settings, schema

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/signin")
credentials_exception = HTTPException(
    status_code=401,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": schema.TokenTypeEnum.bearer},
)


def decode_token(token: str):
    try:
        decoded_token = jwt.decode(token, settings.JWT_SECRET, algorithms="HS512")
    except JWTError:
        raise credentials_exception
    return decoded_token


class DecodedTokenUser:
    def __init__(self, token: str = Depends(oauth2_scheme)):
        decoded_token = decode_token(token)
        if decoded_token.get("membership_id"):
            self.user_id = uuid.UUID(int=decoded_token.get("user_id"))
        else:
            raise credentials_exception
