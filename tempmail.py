import requests
import random
import string

# 獲取可用的域名列表
domains_url = "https://api.mail.tm/domains"
response = requests.get(domains_url)

if response.status_code == 200:
    domains = response.json()['hydra:member']
    domain = domains[0]['domain']  # 選擇第一個域名
    print(f"Available domain: {domain}")
else:
    print(f"Failed to get domains: {response.status_code}")


# 生成隨機的郵箱名
def generate_random_string(length=10):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
username = generate_random_string()
email = f"{username}@{domain}"

# 設定帳號信息
account_data = {
    "address": email,
    "password": "qwer1234"
}

# 創建帳號
account_url = "https://api.mail.tm/accounts"
response = requests.post(account_url, json=account_data)

if response.status_code == 201:
    print(f"Account created: {email}")
else:
    print(f"Failed to create account: {response.status_code} - {response.text}")


login_url = "https://api.mail.tm/token"
login_data = {
    "address": email,
    "password": "qwer1234"
}
response = requests.post(login_url, json=login_data)

if response.status_code == 200:
    token = response.json()['token']
    print(f"Login successful. Token: {token}")
else:
    print(f"Failed to login: {response.status_code} - {response.text}") 
    
headers = {
    "Authorization": f"Bearer {token}"
}

# 獲取郵件
messages_url = "https://api.mail.tm/messages"
response = requests.get(messages_url, headers=headers)
if response.status_code == 200:
    emails = response.json()
    print(emails)
    
else:
    print(f"Failed to retrieve emails: {response.status_code} - {response.text}")       