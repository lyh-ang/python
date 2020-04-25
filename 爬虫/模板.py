import requests
from bs4 import BeautifulSoup
address = '结果.txt'
def check_connection():
    try:
        r = requests.get('https://www.bilibili.com/')
        r.raise_for_status()  #如果返回不是200则引发
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '出现异常'

data = check_connection()
soup = BeautifulSoup(data,'html.parser')
print(soup)
with open(address,'w') as objet_file:
    objet_file.write(check_connection())