from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse

from app.const import APP_DESCRIPTION
from app.infrastructure.logger import Logger
from app.router.menu_router import menu_router
from app.router.order_router import order_router
from app.settings import Settings

log = Logger(class_name=__name__)

settings = Settings()


app = FastAPI(
    title=f"{settings.app_name} - {settings.app_description}",
    description=APP_DESCRIPTION,
    summary="Mashgin Restaurant Project",
    version="0.0.1",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(menu_router)
app.include_router(order_router)


@app.get("/", response_class=PlainTextResponse, tags=["Health"])
async def main():
    return f"{settings.app_name} - {settings.app_description}"


@app.get("/health", tags=["Health"])
async def health():
    return {"message": "Working route!!"}
