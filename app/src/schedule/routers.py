from fastapi import APIRouter

from schedule.handler import parse_query

router = APIRouter()


@router.get("/schedule/planes/date/{date}/city/{city_from}/{city_to}")
async def read_schedule(date, city_from, city_to):
    return parse_query(date, city_from, city_to)
