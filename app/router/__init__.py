from fastapi import APIRouter

from app.router import api_v1

router = APIRouter()

router.include_router(api_v1.router, prefix="/v1")
