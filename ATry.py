import requests
import json
r=requests.get('https://api.eatrice.top/reading')
print(r.text.Content)