import requests

r = requests.get('http://papi.icbc.com.cn/exchanges/ns/getLatest')
print(r.content.decode('utf-8'))