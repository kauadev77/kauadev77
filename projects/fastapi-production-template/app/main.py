from fastapi import FastAPI

from app.api.v1.routes import router
from app.core.config import settings

def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_name, version="1.0.0")
    app.include_router(router)
    return app

app = create_app()
