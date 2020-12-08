#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

변동폭 = float(btc['max_price']) - float(btc['min_price']) # float 함수를 사용해 정수를 소수값으로 바꿔 정밀한 계산을 할 수 있도록 함
시가 = float(btc['opening_price'])                         # 시가,변동폭, 최고가의 정의를 명시된 key name을 이용하여 정의
최고가 = float(btc['max_price'])                           # if 함수를 이용하여 (시가 + 변동폭)이 최고가 보다 높을 경우 "상승장", 
그렇지 않은 경우 "하락장" 문자열을 출력하라.               #  그렇지 않을 때 "하락장" 문자열을 출력한다. ( 

if (시가+변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")

