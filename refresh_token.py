from client import *

_, refresh_token = get_token()

payload = {
    'grant_type': 'refresh_token',
    'refresh_token': refresh_token,
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
}

response = requests.post(TOKEN_URL, data=payload)

if response.status_code == 200:
    print(response.json())
    access_token = response.json()['access_token']
    # 使用新的 Access Token 进行后续操作
else:
    # 处理错误情况，例如无效的 Refresh Token 或客户端凭据
    print(response.json())
