import requests
from client import get_token

test_url = 'http://127.0.0.1:8000/img'
access_token = get_token()
# print(access_token)
headers = {
    'Authorization': f'Bearer {access_token}'
}
response = requests.get(test_url, headers=headers)
print(response)
with open('1.png', 'wb') as f:
    f.write(response.content)
