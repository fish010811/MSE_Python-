#!/usr/bin/env python
# coding: utf-8

# In[1]:


def 함수0(num) :           #  c = 함수2(2) = 함수1(12)= 함수0(14) 
    return num * 2        # 함수0은 num * 2 이므로 14 * 2 = 28 이다.

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)

