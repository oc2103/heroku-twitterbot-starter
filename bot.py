import os
import requests

BEARER_TOKEN = os.getenv("BEARER_TOKEN")

def create_headers(token):
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

def tweet(message):
    url = "https://api.twitter.com/2/tweets"
    payload = {"text": message}
    headers = create_headers(BEARER_TOKEN)
    response = requests.post(url, headers=headers, json=payload)
    print(response.status_code, response.text)

if __name__ == "__main__":
    tweet("Hello world from v2 API!")
