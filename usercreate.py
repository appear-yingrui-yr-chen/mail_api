import requests
from playwright.sync_api import sync_playwright
import time
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
        if email['from']['address'] =='airis@appier.com':
            mail_id=email['id']
            realresponse=requests.get(messages_url+"/"+mail_id,headers=headers)
            targetmail=realresponse.json()
            theuser=targetmail['to'][0]['address']
            print(theuser)
            start=targetmail['intro'].find("join")+9
            endpoint=targetmail['intro'].find("project")-1
            project=targetmail['intro'][start:endpoint]
            print(f"project name: {project }")
            start2=targetmail['text'].find("link")+7
            endpoint2=targetmail['text'].find("create")-5
            thelink=targetmail['text'][start2:endpoint2]
            print(thelink)
            break
           
        
else:
    print(f"Failed to retrieve emails: {response.status_code} - {response.text}")       


with sync_playwright() as p:
    # 啟動 Chromium 瀏覽器
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # 打開 連結
    page.goto(thelink)
    
    # 處理可能出現的隱私提示
    if page.locator("text=接受所有").is_visible():
        page.click("text=接受所有")  # 如果有隱私提示，點擊「接受」

    # 使用選擇器等加載完成
    page.wait_for_selector("input[name='first_name']")
    # 填入辦帳號所需內容
    page.fill("input[name='first_name']", "tester")
    page.fill("input[name='last_name']", "user")
    page.fill("input[placeholder='Enter your company name']","Appier")
    page.click("text='Company size...'")
    page.wait_for_selector("text='51-250'")
    page.click("text='51-250'")
    password="Qwer1234"
    page.fill("input[name='password']", password)
    page.click("label:has-text('I have read and agree to the')")
    page.click("text='Industry...'")
    page.wait_for_selector("text='SaaS'")
    page.click("text='SaaS'")
    page.click("text='Department...'")
    page.wait_for_selector("text='Other'")
    page.click("text='Other'")
    page.click("text='Continue'")

    #登入
    page.wait_for_selector("input[name='username']")
    page.fill("input[name='username']", theuser)
    page.fill("input[name='password']",password)
    page.click("text='繼續'")

    time.sleep(500)
