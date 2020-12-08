#!/usr/bin/env python
# coding: utf-8

# In[1]:


data = tuple(range(2,100,2))
print(data)
# range 함수는 range(start, stop, step) 으로 구성된다. start 를 포함하여 stop까지 정수를 표시하는데 이때 stop 에 해당되는 정수는
# 포함하지 않고 나타낸다. 마지막 step 부분은 숫자사이의 간격을 나타내며 음수 지정도 가능하다.
# range함수 사용 예시 
# range(0, 20, 2) = 0, 2, 4, 6, 8, 10, 12, 14, 16, 18
# 여기서 문제에 제시된 data는 리스트 였기 때문에 tuple() 함수를 이용해서 튜플로 바꿔주는 과정이 들어간다.





