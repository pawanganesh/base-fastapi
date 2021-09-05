from fastapi import APIRouter

from app.router.api_v1 import login, users, utils

router = APIRouter()
router.include_router(login.router, tags=["login"])
router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(utils.router, prefix="/utils", tags=["utils"])
