import requests
import json

url = "https://www.codegrepper.com/api/search_term_alternatives.php?q={query}"

headers={
"Content-Type": "application/json"
}
    
response = requests.get(url,    headers=headers)


if response.status_code != 200:
    print("Server returned an invalid response")
else:
    res = response.json()
    print(res['related_terms'])