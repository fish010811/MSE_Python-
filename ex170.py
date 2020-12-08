#!/usr/bin/env python
# coding: utf-8

# In[14]:


j = 1
for i in range(1,11) : # i 라는 변수를 1부터 10까지 나열되게 루프가 생성된다.
    j = j + i          #  range(1, 11) 값인 1부터 10까지가 게속 j 값에 더해지며 코드가 실행된다.
    print(j)           #예시 j -> 1일때, i -> 2, j = j + i 에 의해 j = 2 가되고, 다시 i -> 3 , j -> 6  이상태로 ㅑ = 10 까지 반복

