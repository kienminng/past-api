from pydantic.v1 import BaseModel

from pydantic import BaseModel
class TokenData(BaseModel):
    username: str
    role: str

    class Config:
        from_attributes = True