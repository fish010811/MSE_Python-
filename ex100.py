#!/usr/bin/env python
# coding: utf-8

# In[3]:


date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date,close_price))
print(close_table)
# 먼저 dict 함수는 항목이 없는 새 딕셔너리를 만드는 함수이다. 그곳에 zip 함수를 이용한다.
# zip 함수는 동일한 갯수의 요소값을 갖는 시퀀스 자료형을 묶어주는 역할을 한다.
# 이때 date 와 close_price 의 순서를 바꾸면 key와 value도 변경된다.

