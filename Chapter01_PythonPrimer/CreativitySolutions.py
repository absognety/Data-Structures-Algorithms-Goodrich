
# coding: utf-8

# In[2]:

#C-1.13

def ReversE(X):
    return (X[::-1])

v = [8,1,10,-12,7,1,0,2,-16,-38,20]

print (list(reversed(v)))
print (ReversE(v))
v.reverse()
print (v)


# In[3]:

#C-1.14

def odd_product(X):
    pairs=[]
    for i in X:
        for j in X[1:]:
            if ((i*j)%2 != 0):
                if (i!=j):
                    if ((i,j) not in pairs):
                        pairs.append((i,j))
    return pairs

test = [3,7,0,9,1,2,4,13,29,31,37,10,11,16]
print (odd_product(test))


# In[5]:

#C-1.15

def distinct_check(X):
    dist_nums = []
    for i in X:
        if i not in dist_nums:
            dist_nums.append(i)
    return dist_nums

dist_nums = distinct_check([2,3,4,5,1,1,2,1,1.5,0,1,7,1])
print (dist_nums)

if dist_nums:
    print ('Duplicity Exists')
else:
    print ('No duplicates, all are distinct')


# In[6]:

#C-1.16

def scale(data, factor):
    for j in range(len(data)):
        data[j]*=factor
    return (data)

X = [100,120,108,156,171,139,184]
scale(X,0.5)


# + X is an actual parameter, data is a formal parameter
# + when the caller gives out a function call, the assignment of instances are done (data=X,factor=0.5) which are operated under local scope of the function `scale`

# In[7]:

#C-1.17

def scale(data,factor):
    new=[]
    for val in data:
        val *= factor
        new.append(val)
    return (data,new)

X=[1000,8018,1578,7821,1820,3821,7319,6197,4382]
scale(X,0.86)


# + As you can observe here, the actual parameter given by caller is not altered but the new instance created under the scope of function is desired result obtained after scaling
# 
# + This is due to the fact that, we are not altering the original data entered by caller but extracting the elements one by one using iterator `val` and thereby altering it.

# In[5]:

#C-1.18

iterms = 0
seq = []
for i in range(10):
    iterms = iterms + (2*i)
    seq.append(iterms)
print (seq)
seq_new = [k*(k-1) for k in range(1,11)]
print (seq_new)


# In[14]:

#C-1.19

import string
test = string.ascii_lowercase

print (list(test))


# In[8]:

#C-1.20

import random

X = [2,4,6,10,-3,-12,10,29,83,28,13,56,67,74]
random.shuffle(X)
print (X)
random.shuffle(X)
print (X)

def shuff(data):
    for i in range(0,len(data)):
        rand_ind = random.randint(0,i)
        var = data[rand_ind]
        data[rand_ind] = data[i]
        data[i] = var
    return (data)
print (shuff(X))


# In[ ]:

#C-1.21

data = []
done = False
while not done:
    try:
        entry = input('Enter an input from client side, Standard input is collected\n')
        data.append(entry)
    except EOFError:
        for i in range(len(data)-1,-1,-1):
            print (data[i])
            done = True


# In[11]:

#C-1.22
import numpy as np

a = list(map(int,input().strip().split()))
b = list(map(int,input().strip().split()))

c = np.multiply(a,b)
print (c)

_c_ = [0]*len(a)
for i in range(len(a)):
    _c_[i] = a[i]*b[i]
_c_


# In[13]:

#C-1.23

c = ['']*30
try:
    for i in range(60):
        c[i] = i*0.5
except IndexError:
    print ('Don’t try buffer overflow attacks in Python')
c


# In[17]:

#C-1.24

sample = 'Hello world! I am your natural language UI Jarvis'
sample = sample.lower()
print (sample)
print ('Number of vowels is {0}'.format(sample.count('a')+sample.count('e')+sample.count('i')+sample.count('o')+sample.count('u')))


# In[25]:

#C-1.25

import re
strg = "Let's try, Mike! eventhough we know it is a long shot"
tokens = strg.split()
strg = [''.join(re.split("[ .,;:!?‘’``''@#$%^_&*()<>{}~\n\t\\\-]", word)) for word in tokens]
strg = ' '.join(strg)
strg


# In[30]:

#C-1.26

a = int(input())
b = int(input())
c = int(input())

if ((a+b)==c):
    print ('a+b=c')
elif ((a==(b-c))):
    print ('a=b-c')
elif ((a*b)==c):
    print ('a*b=c')
else:
    print ('not in the given choices')


# In[35]:

#C-1.28

import math

def norm(v,p=2):
    magn = 0
    for i in range(len(v)):
        magn = magn + math.pow(v[i],p)
    magn = math.pow(magn,1/p) 
    return magn
print (norm((3,4)))
print (norm((1,2,3)))
print (norm((3,4,5),3))

