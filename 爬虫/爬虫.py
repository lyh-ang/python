import requests
from bs4 import BeautifulSoup
address = '结果.txt'
def check_connection():
    try:
        r = requests.get('https://qxzx.yunxx.com/views/myroom/livecourse.html?cwid=8520787&courseId=1254640')
        r.raise_for_status()  #如果返回不是200则引发
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '出现异常'

data = check_connection()
print(BeautifulSoup(data,'html.parser'))
with open(address,'w') as objet_file:
    objet_file.write(check_connection())