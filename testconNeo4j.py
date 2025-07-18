import requests
import base64
from requests.auth import HTTPBasicAuth

# Neo4j 连接信息
neo4j_url = "http://localhost:7474/db/neo4j/tx/commit"
username = "neo4j"
password = "1021albb??"  # 注意：这是从您的base64解码得到的密码

# 准备请求头
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    # 两种授权方式任选其一
    # "Authorization": "Basic bmVvNGo6MTAyMTM4NjY1MA=="  # 直接使用您提供的base64
    # 或者使用HTTPBasicAuth自动生成
}

# 准备一个简单的Cypher查询
cypher_query = {
    "statements": [{
        "statement": "MATCH (n) RETURN n LIMIT 5"
    }]
}

try:
    # 发送POST请求
    response = requests.post(
        neo4j_url,
        json=cypher_query,
        headers=headers,
        auth=HTTPBasicAuth(username, password)  # 使用基本认证
    )

    # 检查响应
    if response.status_code == 200:
        print("连接成功！响应数据：")
        print(response.json())
    else:
        print(f"连接失败，状态码：{response.status_code}")
        print("响应内容：", response.text)

except requests.exceptions.RequestException as e:
    print("请求出错：", str(e))
except Exception as e:
    print("发生错误：", str(e))