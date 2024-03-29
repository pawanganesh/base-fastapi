from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.router import router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_STR}/openapi.json",
    version="1.0.0",
    description="Boilerplate code for quick implementation of REST API with JWT Authentication"
                " using FastAPI and PostgreSQL."
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            str(origin) for origin in settings.BACKEND_CORS_ORIGINS
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(router, prefix=settings.API_STR)
