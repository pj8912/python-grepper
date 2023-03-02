import requests
import json
from token_id import token, user_id

def get_answers(query):
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
        return res['answers']
        # for i in res['answers']:
        #     print(i.get('answer'), '\n')
