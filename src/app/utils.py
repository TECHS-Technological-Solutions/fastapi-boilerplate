import hashlib
import logging

from jose import jwt

from app import schema, settings

logger = logging.getLogger(__name__)


def decode_auth_token_from_headers(headers: dict) -> dict:
    token = headers.get('authorization')
    if token:
        token = token.removeprefix(f'{schema.TokenTypeEnum.bearer} ')
        decoded = jwt.decode(
            token,
            key=settings.JWT_SECRET,
            algorithms=[schema.JWT_ALGORITHM, ],
            options={
                'verify_exp': False,
            }
        )
        return decoded
    return {}


def calculate_md5_hash(string):
    _hash = hashlib.md5()  # nosec
    _hash.update(string.encode('UTF-8'))
    return _hash.hexdigest()


def calculate_sha256_hash(string):
    _hash = hashlib.sha256()  # nosec
    _hash.update(string.encode('UTF-8'))
    return _hash.hexdigest()
