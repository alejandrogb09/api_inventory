import requests
from config import BASE_URL, USERNAME, PASSWORD

def get_token():
    response = requests.post(
        f"{BASE_URL}/token/",
        json={
            "username": USERNAME,
            "password": PASSWORD
        }
    )

    response.raise_for_status()
    return response.json()["token"]