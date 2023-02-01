import requests
import json

def get_answers(query):
    token = "87cf3101746ccc7d237e83f60173ec1435a93e4e4be35272435000672099bca1fac08301035ef62e1bd413d4c6a8bb9e267080da4ec792e73d621b1c5acd8d37"
    user_id = "85648"

    #required : search term, and search options
    
    url = f'https://www.codegrepper.com/api/search.php?q={query}&search_options=search_titles'

    headers = {
        "Content-Type": "application/json",
        "x-auth-token": token,
        "x-auth-id": user_id
    }
    
    response = requests.post(url, headers=headers)
    

    if response.status_code != 200:
        print("Server returned an invalid response")
    else:
        res = response.json()
        for i in res['answers']:
            print(i.get('answer'), '\n')


get_answers('PHP')


