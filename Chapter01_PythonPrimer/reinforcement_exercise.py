#%% 
#1.12 Reinforcement
#R-1.1

n = int(input())
m = int(input())

def is_multiple(p,q):
    """
    Write a short Python function, is multiple(n, m), that takes two integer
    values and returns True if n is a multiple of m, that is, n = mi for some
    integer i, and False otherwise.
    
    """ 
    if (p%q == 0):
        return True
    return False

print (is_multiple(n,m))

#%% R-1.2
    
num = input()

def is_even(number):
    
    """
    Write a short Python function, is even(k), that takes an integer value and
    returns True if k is even, and False otherwise. However, your function
    cannot use the multiplication, modulo, or division operators.
    
    """
    ent = number
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
        
print (is_even(num))

#%%

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

#%%
#R-1.4
        
def sum_squares(n):
    if (n<0):
        print ('Not a valid entry')
    elif (n==0):
        return 0
    else:
        f = n*(n+1)*((2*n)+1)/6
        g = n**2
        return (f-g)
    
#%%
#R-1.5

import numpy as np

def sum_command(n):
    seq = np.array(range(n))
    seq = seq**2
    return (seq.sum())

#%%
    
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
    
#%%
    
#R-1.7
import numpy as np

def sum_odd_pos_command(n):
    seq = list(range(n))
    seq = np.array([i for i in seq if i%2!=0])
    seq = seq**2
    return (seq.sum())

#%%

    

