from fastapi import FastAPI

from .http_client import CMCHTTPClient

from dashboard.src.config import settings

from .router import router as router_crypto

app = FastAPI()

app.include_router(router_crypto)