import logging

from fastapi import Request, HTTPException, Depends
from starlette.authentication import (
    AuthenticationBackend, SimpleUser, AuthCredentials, UnauthenticatedUser
)

from app.db import create_session, SessionLocal
from app.utils import decode_auth_token_from_headers

logger = logging.getLogger(__name__)


class AuthorizedUser(SimpleUser):
    def __init__(self, roles, *args, **kwargs):
        self.roles = roles
        super().__init__(*args, **kwargs)


class UnauthorizedUser(UnauthenticatedUser):
    def __init__(self, *args, **kwargs):
        self.roles = []
        super().__init__(*args, **kwargs)


class BasicAuthBackend(AuthenticationBackend):
    async def authenticate(self, request):  # noqa
        roles = []
        auth = request.headers.get("authorization")
        if not auth:
            # equal to creating UnauthenticatedUser user
            return None, UnauthorizedUser()

        return AuthCredentials(["authenticated"]), AuthorizedUser(roles, "Authorized User")


class Permission:
    """
    Generic permission
    """
    def __call__(self, request: Request, dbsession: SessionLocal = Depends(create_session)):
        try:
            decoded_auth_headers = decode_auth_token_from_headers(request.headers)
            path = request.url.path
            method = request.method.lower()
            # Check data. `print` is just a placeholder function here.
            print(decoded_auth_headers + path + method)
        except AttributeError as e:
            logging.info(e.__str__())
            raise HTTPException(status_code=403, detail='Invalid user.')
        except Exception as e:
            logging.info(e.__str__())
            raise HTTPException(status_code=403, detail='User does not have permission to access this resource.')


permission = Permission()
