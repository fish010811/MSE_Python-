#!/usr/bin/env python
# coding: utf-8

# In[2]:


class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):     # 자식 클래스가 생성될 때 "자식생성" 이라고 프린트를 한다 
  def __init__(self):
    print("자식생성")
    super().__init__() # super 함수를 이용하여 부모클래스의 생성자(self)를 호출
    
나 = 자식()  # 자식 클래스의 객체가 호출될 때 생성자가 호출되고 자식 클래스가 출력 된다.
             # 그다음 부모 클래스의 클래스공간에 접근해 super라는 키워드를 통해서 __init__ 를 호출하여 "부모생성" 이 출력된다.

