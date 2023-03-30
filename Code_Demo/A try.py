'''
* ==================================================================
* Description: A try.py
* Copyright (c) Konrad Locas.
* All rights reserved.
* Author: Konrad Locas.
* Date: 2023/02/06 星期一 14:51
* ===================================================================
'''
import requests

url='https://www.youtube.com'
r=requests.get(url)
print(r.status_code)