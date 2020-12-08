#!/usr/bin/env python
# coding: utf-8

# In[3]:


icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
icecream['누가바']
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    icecream['누가바']
KeyError: '누가바'
# 딕셔너리에 없는 키를 인덱싱 했기 때문이다.
# 여기서 key는 '폴라포', '빵빠레', '월드콘', '메로나' 인데 새로운 '누가바' 를 사용했기 때문이다.


# In[ ]:




