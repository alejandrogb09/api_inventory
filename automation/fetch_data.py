import requests
from auth import get_token
from config import BASE_URL

def get_products():
    token = get_token()
    headers = {
        "Authorization": f"Token {token}"
    }

    response = requests.get(
        f"{BASE_URL}/products/",
        headers=headers
    )

    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    products = get_products()
    for product in products:
        print(product["name"], product["stock"])