from fastapi import APIRouter

from app.core.config import settings
from app.schemas import EchoRequest, EchoResponse
from app.services.echo import normalize_message

router = APIRouter(prefix="/v1")

@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@router.get("/ready")
def ready() -> dict[str, str]:
    return {"status": "ready", "environment": settings.environment}

@router.post("/echo", response_model=EchoResponse)
def echo(payload: EchoRequest) -> EchoResponse:
    return EchoResponse(
        message=normalize_message(payload.message),
        environment=settings.environment,
    )
