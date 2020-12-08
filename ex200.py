#!/usr/bin/env python
# coding: utf-8

# In[6]:


ohlc = [["open", "high", "low", "close"], 
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
# 수입금 = 시가 - 종가 (open금액 - close금액)
총_수입금 = 0
for 하루금액 in ohlc[1:]: # [1:]: 는 ohlc 안에서 0 번째인 ["open", "high", "low", "close"] 를 제외한다.
    수입금 = 하루금액[0] - 하루금액[3] # 이 식은 "open" 에 해당하는 부분에서 "close"에 해당하는 부분을 빼는 식이다.
    총_수입금 = 총_수입금 + 수입금    
    
print(총_수입금)

