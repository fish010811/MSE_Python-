#!/usr/bin/env python
# coding: utf-8

# In[1]:


if True :
    if False:    # 2. if true 문 안에 있는 이 if false 문은 if false, 즉 거짓이기 때문에 실행되지 않는다.
        print("1")
        print("2")
    else:        # 3. false 이기 때문에 거짓일때 else가 실행되므로 결과적으로 이부분이 실행된다.
        print("3")
else :
    print("4")   # 1. if true 이기 때문에 처음 if 문이 거짓일때 시행되는 이부분은 실행하지 않는다.
print("5")       # 위에서 실행된 값 3아래에 이부분도 실행된다.

