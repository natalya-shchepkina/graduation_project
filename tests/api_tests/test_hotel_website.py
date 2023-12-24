import random

import allure
import pytest
import requests

from helpers import generate_random_string
from data.user_data import User
from jsonschema import validate


@allure.title("Validation of the scheme for get rooms")
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


@allure.title("Sending a message with empty fields")
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


@allure.title("Sending a message with invalid data")
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


@allure.title("Sending a message with correct data")
def test_send_message():
    body = {"name": User.first_name,
            "email": User.email,
            "phone": User.telephone,
            "subject": "subject",
            "description": generate_random_string(random.randint(20, 2000))}
    response = requests.post("https://automationintesting.online/message/", json=body)

    assert response.status_code == 201


@allure.title("Room reservation")
def test_reservation():
    body = {"bookingdates": {
                 "checkin": "",
                 "checkout": ""},
            "depositpaid": False,
            "firstname": User.first_name,
            "lastname": User.last_name,
            "roomid": "1",
            "email": User.email,
            "phone": User.telephone}
    response = requests.post("https://automationintesting.online/booking/", json=body)

    assert response.status_code == 400
    assert 'must not be null' in response.json()['fieldErrors']


@allure.title("User validation")
def test_user_validation(get_token):
    body = {"token": get_token}
    response = requests.post("https://automationintesting.online/auth/validate", json=body)

    assert response.status_code == 200


@allure.title("Checking the response to a request receive a message")
def test_get_messages():
    response = requests.get("https://automationintesting.online/message/")
    quantity = len(response.json()['messages'])
    index = random.randint(0, quantity-1)

    assert response.status_code == 200
    assert response.json()['messages'][index]['id']
    assert response.json()['messages'][index]['name']
    assert response.json()['messages'][index]['subject']
