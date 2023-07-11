import requests
from config import *
from utils import *
from urllib.parse import urlparse, parse_qs

code_verifier, code_challenge = gen_code_verifier_challenge()
url = f"http://127.0.0.1:8000/o/authorize/?response_type=code&code_challenge={code_challenge}&code_challenge_method=S256&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}"


def get_authorize_code():
    response = requests.get(url)
    if 'admin/login/' in response.url:
        param = {
            "csrfmiddlewaretoken": "lXObKlwc9IJPxACb2WVWjHw9pw7kkw1UibZZMfddoF4MAFnK0SiHix1bDukryDlo",
            "username": "daihui",
            "password": "123",
        }
        cookies = {
            "csrftoken": "7olYc4Rbp7v7dfVJ86xV90Fco8nhohuE"
        }
        response = requests.post(response.url, data=param, cookies=cookies)
        # 解析 URL
        parsed_url = urlparse(response.url)
        # 获取参数部分
        query_params = parse_qs(parsed_url.query)
        # 打印参数部分
        authorize_code = query_params.get('code')
        if authorize_code:
            return authorize_code[0]
