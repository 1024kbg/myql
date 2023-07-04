
import requests

cookie= str(ikuuucookie)
cookie1=cookie.encode("utf-8").decode("latin1")
print(cookie1)
session = requests.Session()

url = 'https://ikuuu.eu/user/checkin'  # 替换为实际签到URL
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'Cookie': 'cookie1',

}
    # 检查登录是否成功
response = session.post(url, headers=headers)
if response.status_code == 200 :
    print('签到成功')
else:
    print('登录失败')

html=requests.post(url=url, headers=headers).text

print(html)
