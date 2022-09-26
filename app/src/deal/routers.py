from fastapi import APIRouter

from deal.contracts import AuthModel

from deal.handler import buy_ticket

router = APIRouter()


@router.post("/deal/{flight_id}")
async def register_deal(flight_id, user: AuthModel):
    return buy_ticket(flight_id, user)