#!/usr/bin/env python
# coding: utf-8

# In[5]:


low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility = []                               # volatility 라는 리스트를 생성
for i in range(len(low_prices)) :            # low_prices의 원소의 개수(5일)로 i 변수의 범위 정함
    diff = high_prices[i] - low_prices[i]    #  변동폭을 diff 라 정의하고  변동폭의 값을 지정한다.
    volatility.append(diff)                  # list.append 메소드 를 사용하여 volatility 리스트에 내용추가
print(volatility)                            # 마지막으로 값을 출력한다.          

