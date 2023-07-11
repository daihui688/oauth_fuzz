from authorize import *


def get_token():
    # 定义请求的参数（字典格式）
    data = {
        "grant_type": GRANT_TYPE,
        "code": get_authorize_code(),
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code_verifier": code_verifier,
        "redirect_uri": REDIRECT_URI
    }
    # 将参数编码为字符串
    encoded_data = "&".join([f"{key}={value}" for key, value in data.items()])
    # 发送 POST 请求
    response = requests.post(TOKEN_URL, data=encoded_data,
                             headers={"Content-Type": "application/x-www-form-urlencoded"})
    # 获取响应结果
    resp_data = response.json()
    access_token = resp_data.get('access_token')
    refresh_token = resp_data.get('refresh_token')
    return access_token, refresh_token


if __name__ == '__main__':
    print(get_token())
