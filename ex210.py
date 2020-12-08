#!/usr/bin/env python
# coding: utf-8

# In[1]:


def message1():             #  def으로 함수를 생성한다.                          
    print("A")              # 맨 밑의 message3() 은 함수 message3을 실행 하라는 뜻이다.

def message2():
    print("B")

def message3():
    for i in range (3) :    # range(3)에 의해 3번 반복된다.
        message2()          #  for 루프 안의 내용은 message2()함수를 출력하고 (B가 출력된다) 그 밑에 C 를 출력하라는 뜻이다.
        print("C")          #  3번 반복후 그 밑에 message1(), 즉 A가 출력된다.
    message1()

message3()


# In[ ]:




