import requests

def test():
    response = requests.get("https://automationintesting.online/room/")
    print(response.json())

def test_2():
    body = {"name":"2","email":"22","phone":"3","subject":"2","description":""}
    response = requests.post("https://automationintesting.online/message/", json=body)
    print(response.json())