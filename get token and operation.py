import requests
email="abazxnwrrq@livinitlarge.net"#隨mail更換
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
