from fastapi import APIRouter
from .v1 import router as api_v1_router

router = APIRouter()


@router.get("/jarvis/v1/health")
@router.get("/health")
async def health_check():
    return ":)"


router.include_router(api_v1_router, prefix="/jarvis/v1")
