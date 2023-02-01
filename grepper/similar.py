import requests
import json



def similar_queries(query):
    url = f"https://www.codegrepper.com/api/search_term_alternatives.php?q={query}"
    headers={
        "Content-Type": "application/json"
    }
    response = requests.get(url,    headers=headers)


    if response.status_code != 200:
        print("Server returned an invalid response")
    else:
        res = response.json()
        return res['related_terms']