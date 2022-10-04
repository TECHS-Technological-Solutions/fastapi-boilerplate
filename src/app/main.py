import logging

import sentry_sdk
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from starlette.middleware.authentication import AuthenticationMiddleware
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

from app import settings
from app.permissions import BasicAuthBackend
from app.middlewares import RequestContextMiddleware


logger = logging.getLogger(__name__)


sentry_sdk.init(dsn=settings.SENTRY_DNS)

ROOT_PATH = settings.MAIN_ROOT_PATH

app = FastAPI(docs_url=f'/{ROOT_PATH}/docs',
              openapi_url=f"/{ROOT_PATH}/openapi.json",
              openapi_tags=settings.API_TAGS_METADATA)

asgi_app = SentryAsgiMiddleware(app)

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=settings.ALLOWED_HOSTS
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    AuthenticationMiddleware,
    backend=BasicAuthBackend()
)

app.add_middleware(RequestContextMiddleware)


@app.get(f'/{ROOT_PATH}/ping')
def read_root():
    return {'ping': True}


# Declare routers here
