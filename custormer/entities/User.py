import re
import uuid

from pydantic.v1 import Field, BaseModel, EmailStr, validator
from custormer.exception.InvalidPhoneNumberException import InvalidPhoneNumberException


class User(BaseModel):
    id : uuid.UUID = Field(default_factory=lambda: uuid.uuid4())
    first_name: str
    last_name: str
    email: EmailStr
    phone: str

    @validator('phone')
    def validate_phone(cls, v):
        regex = r"^(\+)[1-9][0-9\-\(\)\.]{9,15}$"
        if v and not re.search(regex, v, re.I):
            raise InvalidPhoneNumberException("Invalid Phone Number.")
        return v

