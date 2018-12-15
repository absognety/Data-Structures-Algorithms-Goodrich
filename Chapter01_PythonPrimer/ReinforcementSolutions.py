
# coding: utf-8

# # Chapter - 1: Python Primer 
# 
# #### Reinforcement (1.1-1.12)

# In[1]:

#R-1.1

def is_multiple(p,q):
    """
    Write a short Python function, is multiple(n, m), that takes two integer
    values and returns True if n is a multiple of m, that is, n = mi for some
    integer i, and False otherwise.
    
    """ 
    if (p%q == 0):
        return True
    return False

print (is_multiple(6,2))
print (is_multiple(849949492,2))
print (is_multiple(157,3))


# In[2]:

#%% R-1.2

def is_even(number):
    
    """
    Write a short Python function, is even(k), that takes an integer value and
    returns True if k is even, and False otherwise. However, your function
    cannot use the multiplication, modulo, or division operators.
    
    """
    ent = str(number)
    length = len(ent)
    number_check = all(c.isdigit() for c in ent)
    if number_check:
        if ((ent[length-1]=='0') | (ent[length-1]=='2') | 
            (ent[length-1]=='4') | (ent[length-1]=='6') |
            (ent[length-1]=='8')):
            return True
        else:
            return False
    else:
        print ('not a valid number')

print (is_even(784))
print (is_even(563))


# In[3]:

#R-1.3
def max_min(H):
    max_init=H[0]
    for i in H:
        if (max_init < i):
            max_init = i
    min_init=H[0]
    for i in H:
        if (min_init > i):
            min_init = i
    return (max_init,min_init)

def minmax(data):
    
    """
    Write a short Python function, minmax(data), that takes a sequence of
    one or more numbers, and returns the smallest and largest numbers, in the
    form of a tuple of length two. Do not use the built-in functions min or
    max in implementing your solution.
    
    """
    if (type(data)==list):
        return (max_min(data))
    elif (type(data)==tuple):
        return (max_min(data))
    elif (type(data)==set):
        alter_data = list(data)
        return (max_min(alter_data))
    
print (minmax([38,78,13,-4,-19,0,1]))
print (minmax((-26,152,190,-4,0,20,30)))
print (minmax({-8,-18,210,34,82,19,990}))


# In[8]:

#R-1.4

def sum_squares(n):
    if (n<0):
        return ('Not a valid entry')
    elif (n==0):
        return 0
    else:
        f = n*(n+1)*((2*n)+1)/6
        g = n**2
        return (f-g)
    
print (sum_squares(67))
print (sum_squares(49))
print (sum_squares(-46))
print (sum_squares(0))


# In[9]:

#R-1.5

import numpy as np

def sum_command(n):
    seq = np.array(range(n))
    seq = seq**2
    return (seq.sum())

print (sum_command(5))
print (sum_command(100))


# In[1]:

#R-1.6
import numpy as np

def sum_odd_pos(n):
    seq = list(range(n))
    seq = np.array([i for i in seq if i%2!=0])
    seq = seq**2
    total_sum=0
    for i in seq:
        total_sum=total_sum+i
    return (total_sum)

print (sum_odd_pos(5))
print (sum_odd_pos(80))


# In[5]:

#R-1.7
import numpy as np

def sum_odd_pos_command(n):
    seq = list(range(n))
    seq = np.array([i for i in seq if i%2!=0])
    seq = seq**2
    return (seq.sum())

print (sum_odd_pos_command(5))
print (sum_odd_pos_command(80))


# In[3]:

#R-1.8
#j = n + k
seq = 'hey I am good, How are you'
n = len(seq)
k = -5
print (seq[k] == seq[n+k])
k = -4
print (seq[k] == seq[n+k])
k = -n
print (seq[k] == seq[n+k])


# In[4]:

#R-1.9

test = list(range(50,90,10))
#start=50
#stop=90
#step=10
print (test)


# In[6]:

#R-1.10

test = list(range(8,-10,-2))
#start=8
#stop=-10
#step=-2
print (test)


# In[7]:

#R-1.11

test = [2**i for i in range(9)]
print (test)


# In[10]:

#R-1.12

import random
sample1 = random.randrange(1,100,1)
print (sample1)
sample2 = random.choice(list(range(1,100,1)))
print (sample2)

