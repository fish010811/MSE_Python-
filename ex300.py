#!/usr/bin/env python
# coding: utf-8

# In[2]:


per = ["10.31", "0", "8.00"]  
# try:
#    실행 코드
#except:
#    예외가 발생했을 때 수행할 코드
#else:
#    예외가 발생하지 않았을 때 수행할 코드
#finally:
#   예외 발생 여부와 상관없이 항상 수행할 코드 

for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print("clean data")
    finally:
        print("변환 완료")
# 순서대로 "10.31", "0", "8.00" 이 for루프안에서 try, except, else, finally를 거쳐 계산된다.


# In[ ]:




