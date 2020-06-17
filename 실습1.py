#!/usr/bin/env python
# coding: utf-8

# In[21]:


int1 = int(input("첫 번째 정수: "))
int2 = int(input("두 번째 정수: "))
int3 = input("연산자: ")

if int3 == "+":
 print(int1,int3,int2,"=",int1+int2)
    
elif int3 == "-":
 print(int1,int3,int2,"=",int1-int2)
     
elif int3 == "*":
 print(int1,int3,int2,"=",int1*int2)
            
elif int3 == "/": 
 print(int1,int3,int2,"=",int1/int2)

elif int3 == "%": 
 print(int1,int3,int2,"=",int1%int2)
                
else:
 print("사칙연산 외 다른 것을 입력하셨습니다. 다시 입력하세요")
                    

                    
                


# 

# In[ ]:





# In[ ]:




