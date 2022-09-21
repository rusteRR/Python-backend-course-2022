from typing import Union

from fastapi import APIRouter

import contracts

router = APIRouter()


@router.get("/users")
async def read_user_me():
    return {"user_id": "the current user"}


@router.get("/users/{username}")
async def read_user(username: str):
    return {"user_name": username}


@router.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@router.post("/users/")
async def create_item(user: contracts.User):
    request_dict = user.dict()
    if user.age < 18:
        request_dict.update({"cost": 0})
    return request_dict
