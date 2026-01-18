import requests

API_TOKEN = "sk_live_51Nf9x9Kp0xA1QZ9Yw2K8QbH2R3f7Z9"  # INTENTIONAL

def call_api():
    # token digunakan ke sink
    return requests.get(
        "https://api.example.com/data",
        headers={"Authorization": f"Bearer {API_TOKEN}"}
    )
