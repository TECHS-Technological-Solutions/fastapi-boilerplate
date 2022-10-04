from contextvars import ContextVar

from fastapi import Request
from starlette.responses import PlainTextResponse
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from app import schema


REQUEST_USER = "request_user"

_request_user_ctx_var = ContextVar(REQUEST_USER, default=None)


def get_request_user():
    """
    get the request user data
    """
    return _request_user_ctx_var.get()


class RequestContextMiddleware(BaseHTTPMiddleware):
    """
    Get context from request
    """

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ):
        membership = None

        token = request.headers.get('authorization')
        if token:
            token = token.removeprefix(f'{schema.TokenTypeEnum.bearer} ')
            # auth_token_data = jwt.decode(token, key=settings.JWT_SECRET,
            #                              algorithms=[schema.JWT_ALGORITHM, ],
            #                              options={'verify_exp': False})
        token = _request_user_ctx_var.set(membership)
        try:
            response = await call_next(request)
        except Exception as e:  # noqa
            response = PlainTextResponse(e.__str__(), status_code=403)

        _request_user_ctx_var.reset(token)

        return response
