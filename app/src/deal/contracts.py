from pydantic import BaseModel


class AuthModel(BaseModel):
    name: str
    age: int
    login: str
