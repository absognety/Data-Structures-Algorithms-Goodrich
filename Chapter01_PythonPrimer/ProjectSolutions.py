
# coding: utf-8

# ### Chapter-1: Python Primer
# 
# ###### Project Solutions (1.29-1.36)

# In[9]:

#P-1.29

import itertools
chars = ['c','a','d','t','o','g']
chars = ''.join(chars)
strgs = itertools.permutations(chars,6)
list(strgs)


# In[10]:

#P-1.30

x = int(input())
cnt = 0
while (x/2 > 2):
    cnt=cnt+1
    x = x/2
print (cnt)


# In[ ]:

#P-1.32

result=0
cnt=0
while (True):
    n = int(input())
    operator = input()
    if n and operator:
        if operator=='+':
            cnt+=1
            result=result+n
        elif operator=='-':
            cnt+=1
            result=n-result
        elif operator=='*':
            cnt+=1
            if (cnt>1 and result!=0):
                result=result*n
            else:
                result=(result+1)*n
        elif operator=='/':
            cnt+=1
            if (cnt>1 and result!=0):
                result=result/n
            else:
                result=n/(result+1)
        elif operator=='=':
            print (result)
            break
    else:
        print ('Invalid entry in either of the two entities')
        break


# In[22]:

#P-1.35

import datetime
import random

def random_date():
    year = random.randint(1995,2000)
    month = random.randint(1,12)
    day = random.randint(1,28)
    birthday = datetime.datetime(year,month,day)
    return birthday

def bday_simulations(n):
    birthdays_n = [random_date() for person in range(n)]
    uniq_birthdays = list(set(birthdays_n))
    print ('Number of birthdays generated:',len(birthdays_n))
    print ('Number of unique birthdays generated:',len(uniq_birthdays))
    pass

print (bday_simulations(5))
print (bday_simulations(10))
print (bday_simulations(15))
print (bday_simulations(20))
print (bday_simulations(25))
print (bday_simulations(30))
print (bday_simulations(35))
print (bday_simulations(40))
print (bday_simulations(45))
print (bday_simulations(50))
print (bday_simulations(55))
print (bday_simulations(60))
print (bday_simulations(65))
print (bday_simulations(70))
print (bday_simulations(75))
print (bday_simulations(80))
print (bday_simulations(85))
print (bday_simulations(90))
print (bday_simulations(95))
print (bday_simulations(100))


# In[12]:

#P-1.36

sample_string = input().strip().split()
uniq_string = list(set(sample_string))
for s in uniq_string:
    print (s,sample_string.count(s))


# In[ ]:



