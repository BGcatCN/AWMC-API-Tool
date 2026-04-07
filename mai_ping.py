import os
import requests
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 获取 Bearer 令牌
bearer_token = os.getenv('BEARER_TOKEN')

if not bearer_token:
    print("错误：.env文件中缺少BEARER_TOKEN")
    exit(1)

# awmc.cc API
url = "https://api.awmc.cc/v1/mai_ping"

# 设置请求头
headers = {
    'Authorization': f'Bearer {bearer_token}'
}

# 发送GET请求
try:
    response = requests.get(url, headers=headers)
    print("响应状态码:", response.status_code)

    try:
        data = response.json()
    except ValueError:
        data = None

    if data is not None:
        print("响应内容:", data)
        result = data.get('result')
        if result == 'Pong':
            print("API正常")
        elif result == 'down':
            print("API故障")
        else:
            print("未知结果:", result)
    else:
        print("响应内容:", response.text)
except Exception as e:
    print("请求失败:", str(e))