import requests
import json


def fetch_terms():
    token = "87cf3101746ccc7d237e83f60173ec1435a93e4e4be35272435000672099bca1fac08301035ef62e1bd413d4c6a8bb9e267080da4ec792e73d621b1c5acd8d37"
    user_id = "85648"

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
        # for i in res:
        #     terms = i.get("term", None)
        #     bonus_points = i.get('bonus_points',None)
        #     #print(terms, '| bonus_points[' ,bonus_points,']', '\n')
        #     return i



