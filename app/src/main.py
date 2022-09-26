from fastapi import FastAPI

from schedule.routers import router as schedule_router
from auth.routers import router as auth_router
from deal.routers import router as deal_router

app = FastAPI(
    title="FTicket",
    description=("FTicket"),
    version="0.0.1",
    docs_url="/docs",
    redoc_url="/docs/redoc",
)

app.include_router(schedule_router)
app.include_router(auth_router)
app.include_router(deal_router)
