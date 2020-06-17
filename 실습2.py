#!/usr/bin/env python
# coding: utf-8

# In[24]:


num  = int(input("번호: "))
kor  = int(input("국어점수: "))
eng  = int(input("국어점수: "))
mat  = int(input("수학점수: "))
psy  = int(input("물리점수: "))
total = kor + eng + mat + psy
avg = total/4


if avg >= 90.0:
    grade = 'A'
elif avg >= 80.0:
    grade = 'B'
elif avg >= 70.0:
    grade = 'C'
elif avg >= 60.0:
    grade = 'D'
else:
    grade = 'F'
        
print("==========================================")
print("번호  국어  영어  수학  물리   총점    평균    학점")
print(num," ",kor," ",eng," ",mat," ",psy," ",total," ",avg," ",grade)
print("==========================================")


    
    

 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




