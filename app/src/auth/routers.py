from re import A
from fastapi import APIRouter

from auth.contracts import AuthModel

from auth.handler import register

router = APIRouter()


@router.post("/auth/register")
async def auth(user: AuthModel):
    return register(user)