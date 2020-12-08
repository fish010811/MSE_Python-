#!/usr/bin/env python
# coding: utf-8

# In[18]:


리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for 변수 in 리스트:
    이름, ext = 변수.split('.')  # '.'을 기준으로 변수 분리, # 이름과 ext로 분리
    if ext == 'h' or ext == 'c':    # 확장자가 'h' , 'c' 이면 변수인 리스트 안의 값 출력
        print(변수)                  # 변수는 파일이름과 확장자를 바운딩하고 있음.


# In[ ]:




