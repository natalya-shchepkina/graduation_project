import random

import pytest
import requests

from helpers import generate_random_string
from data.user_data import User
from jsonschema import validate


def test_api_json_schema():
    response = requests.get("https://automationintesting.online/room/")

    schema = {
        "type": "object",
        "properties": {
            "rooms": {
                "type": "array",
                "properties": {
                    "roomid": {"type": "number"},
                    "roomName": {"type": "string"},
                    "type": {"type": "string"},
                    "accessible": {"type": "boolean"},
                    "image": {"type": "string"},
                    "description": {"type": "string"},
                    "features": {"type": "array"},
                    "roomPrice": {"type": "number"}
                }
            }
        }
    }

    validate(instance=response.json(), schema=schema)


@pytest.mark.parametrize("field_error", [
    "Phone may not be blank",
    "Subject may not be blank",
    "Name may not be blank",
    "Message must be between 20 and 2000 characters.",
    "Message may not be blank",
    "Subject must be between 5 and 100 characters.",
    "Phone must be between 11 and 21 characters.",
    "Email may not be blank"
])
def test_empty_send_message(field_error):
    body = {"name": "",
            "email": "",
            "phone": "",
            "subject": "",
            "description": ""}
    response = requests.post("https://automationintesting.online/message/", json=body)

    assert response.status_code == 400
    assert field_error in response.json()['fieldErrors']


@pytest.mark.parametrize("description_length", [19, 2001])
@pytest.mark.parametrize("phone_length", [10, 22])
@pytest.mark.parametrize("email", [
    "test",
    "testmail.ru",
    "test@.mail",
    "test@yandex."
])
def test_sending_invalid_messages(phone_length, email, description_length):
    body = {"name": "name",
            "email": email,
            "phone": generate_random_string(phone_length),
            "subject": "subject",
            "description": generate_random_string(description_length)}
    response = requests.post("https://automationintesting.online/message/", json=body)

    assert 'must be a well-formed email address' in response.json()['fieldErrors']
    assert 'Phone must be between 11 and 21 characters.' in response.json()['fieldErrors']
    assert 'Message must be between 20 and 2000 characters.' in response.json()['fieldErrors']


def test_send_message():
    body = {"name": User.first_name,
            "email": User.email,
            "phone": User.telephone,
            "subject": "subject",
            "description": generate_random_string(random.randint(20, 2000))}
    response = requests.post("https://automationintesting.online/message/", json=body)

    assert response.status_code == 201

