import requests

url_token = 'http://127.0.0.1:8000/api/token/'
data = {
    "username": "qwe",
    "password": "123"
}
response = requests.post(url_token, json=data)
autr = response.json().get('access')
print(autr)
url = "http://127.0.0.1:8000/comentarie/"
headers = {
    "Authorization": f"Bearer {autr}"
}
data = {
    'cvyaz':1,
    'name':'gxhd'
}
#
response = requests.post(url, data=data,headers=headers)
print(response.json())
