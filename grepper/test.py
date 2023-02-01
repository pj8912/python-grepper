import requests
import json 

token = "87cf3101746ccc7d237e83f60173ec1435a93e4e4be35272435000672099bca1fac08301035ef62e1bd413d4c6a8bb9e267080da4ec792e73d621b1c5acd8d37"
user_id = "85648"

data = {
  "answer": "String",
  "user_id": "Number",
  "team_ids": "Number",
  "language": "String",
  "is_private": "Boolean",
  "source_url": "String",
  "codeSearch": {
    "results": "Array",
    "search": "String",
  },
}



url = "https://www.codegrepper.com/api/save_answer.php"

headers = {
  "Content-Type": "application/json",
  "x-auth-token": token,
  "x-auth-id": user_id,
}


response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code != 200:
  print("Server returned an invalid response")
else:
  print(response.json())




