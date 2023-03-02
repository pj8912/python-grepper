import requests
import json
from token_id import token, user_id

def fetch_terms():

    url = "https://www.codegrepper.com/api/get_terms_needing_answers.php"
    headers = {
        "Content-Type": "application/json",
        "x-auth-token": token,
        "x-auth-id": user_id
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Server returned an invalid response")
    else:
        res = response.json()
        return res
          


