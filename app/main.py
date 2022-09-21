from fastapi import FastAPI

from routers import router

app = FastAPI(
    title="HelloWorld",
    description=("HelloWorld"),
    version="0.0.1",
    docs_url="/docs",
    redoc_url="/docs/redoc",
)

app.include_router(router)
