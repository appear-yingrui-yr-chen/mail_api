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
    #print(f"Login successful. Token: {token}")
else:
    print(f"Failed to login: {response.status_code} - {response.text}") 
    
headers = {
    "Authorization": f"Bearer {token}"
}

# 獲取郵件
messages_url = "https://api.mail.tm/messages"
response = requests.get(messages_url, headers=headers)
if response.status_code == 200:
    emails = response.json()['hydra:member']   
    for email in emails:
        if email['from']['address'] =='airis@appier.com': #filter選取寄件者
            mail_id=email['id']
            realresponse=requests.get(messages_url+"/"+mail_id,headers=headers)
            targetmail=realresponse.json()
            print(targetmail['to'][0]['address']) #收件者
            start=targetmail['intro'].find("join")+9
            endpoint=targetmail['intro'].find("project")-1
            print(f"project name: {targetmail['intro'][start:endpoint] }") ＃獲邀project
            start2=targetmail['text'].find("link")+7
            endpoint2=targetmail['text'].find("create")-5
            print(targetmail['text'][start2:endpoint2]) #驗證連結
           
        
else:
    print(f"Failed to retrieve emails: {response.status_code} - {response.text}")       
    
