#!/usr/bin/env python
# coding: utf-8

# In[8]:


def print_max(a, b, c) : # a,b,c 는 정해지지 않은 수
    if a > b and a > c : # if 문을 이용하여 가장 큰 수를 정하는 함수를 완성
        print(a)
    elif b >c and b > a :
        print(b)
    else:                 # 이 else는 위의 else if의 else 부분이라 elif의 내용이 아닐시에 시행된다.
        print(c)
print_max(15, 2, 4)        # 에시를 들어 공식이 제대로 작동하는지 확인
print_max(15, 20, 4)
print_max(15, 20, 38)


# In[ ]:




