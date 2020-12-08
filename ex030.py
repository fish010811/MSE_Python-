#!/usr/bin/env python
# coding: utf-8

# In[2]:


string = 'abcd'
string.replace('b', 'B')
print(string)
# 결과는 'abcd' 그대로이다. 왜냐면 'str', 즉 문자열은 변경할 수 없는 자료형이기 때문이다.
#따라서 replace를 사용해도 'abcd' 가 리턴된다.

