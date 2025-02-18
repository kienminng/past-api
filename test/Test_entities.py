import pytest

from pydantic import ValidationError
from custormer.entities.User import User
from custormer.exception.InvalidPhoneNumberException import InvalidPhoneNumberException


def test_user_create():
    user = User (
        first_name="test",
        last_name="user",
        email="xyz@example.com",
        phone="+25499919191919"
    )
    assert user.first_name == "test"
    assert user.last_name == "user"
    assert user.email == "xyz@example.com"
    assert user.phone == "+25499919191919"

def test_customer_create_throws_invalid_email_exception():

    with pytest.raises(ValidationError) as exc:
        User(
            first_name="test",
            last_name="user",
            email="xyz@exampl",
            phone="+25499919191919"
        )
    assert exc.value.errors()[0]["loc"][0] == "email"
    assert exc.value.errors()[0]["msg"] == "value is not a valid email address"

def test_customer_create_throws_invalid_phone_exception():
    with pytest.raises(InvalidPhoneNumberException) as exc:
        User(
            first_name="test",
            last_name="user",
            email="xyz@exampl",
            phone="+25499919"
        )
    assert isinstance(exc.value, InvalidPhoneNumberException)