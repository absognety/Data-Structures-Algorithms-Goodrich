
# coding: utf-8

# #### R-2.1
# 
# The three main examples of life-critical software applications are:
# 
# 1. ISO 26262
# 2. IEC 62304
# 3. IEC 61513

# #### R-2.2
# 
# Microsoft Office

# #### R-2.3
# 
# 1. Find and Replace - Text editors provide extensive facilities for searching and replacing text, either on groups of files or interactively.Advanced Editors use regular expressions to find or edit text or code.
# 
# 2. Cut, Copy and Paste - Most Text editors provide methods to duplicate or move text within the file or between the files. Ability to handle UTF-8 encoded text.
# 
# 3. Text formatting – Text editors often provide basic formatting features like line wrap, auto-indentation, bullet list formatting using ASCII characters, comment formatting, syntax highlighting etc.
# 
# 4. Undo and redo – As with word processors, text editors provide a way to undo and redo the last edit. Often—especially with older text editors—there is only one level of edit history remembered and successively issuing the undo command will only "toggle" the last change. Modern or more complex editors usually provide a multiple level history such that issuing the undo command repeatedly will revert the document to successively older edits. A separate redo command will cycle the edits...

# In[2]:

#### R-2.4

class Flower():
    """
    Defining a Flower class to construct behaviors and characteristics
    of a flower
    """
    def __init__(self,name,petals,price):
        """
        Constructor method to initialize the inputs to variables
        """
        self._name=name
        self._numpetals=int(petals)
        self._price=float(price)
        
    def Name(self):
        """Returns the name of the flower"""
        return (self._name)
    
    def num_petals(self):
        """Returns the number of petals of the flower"""
        return (self._numpetals)
    
    def Price(self):
        """Returns the price of the flower"""
        return (self._price)
  


flower = Flower('sun flower',10,25.9)
print (flower.Name())
print (flower.num_petals())
print (flower.Price())


# In[6]:

# R-2.5

class CreditCard():
    
    """A Consumer Credit Card"""
    
    def __init__(self,customer,bank,acct,limit):
        """
        Create a new Credit Card Instance
        
        The initial balance is Zero
        customer - the name of the customer (e.g., John Bowman )
        bank - the name of the bank (e.g., California Savings )
        acnt - the acount identifier (e.g., 5391 0375 9387 5309 )
        limit credit limit (measured in dollars)
        
        """
        self._customer = customer
        self._bank = bank
        self._account = acct
        self._limit = limit
        self._balance = 0
         
    def get_customer(self):
        
        """get the name of the customer"""
        
        return (self._customer)
    
    def get_bank(self):
        
        """Returns the bank's name"""
        
        return (self._bank)
    
    def get_account(self):
        
        """Returns the card identifying number (String)"""
        
        return (self._account)
    
    def get_limit(self):
        
        """Returns the current credit limit"""
        
        return (self._limit)
    
    def get_balance(self):
        
        """Returns the current balance"""
        
        return (self._balance)
    
    def charge(self,price):
        
        """
        Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed; False if charge was denied.
        
        """
        if isinstance(price,(int,float)):
            if price + self._balance > self._limit:
                return False
            else:
                self._balance+=price
                return True
        else:
            raise TypeError('Only integers or float values accepted')
        
    def make_payment(self,amount):
        
        """
        Makes payment that reduces balance
        """
        
        if isinstance(amount,(int,float)):
            self._balance = self._balance-amount
        else:
            raise TypeError('only Integers or float values accepted')
        return (self._balance)
        
cc = CreditCard('John Doe', '1st Bank' , '5391 0375 9387 5309' , 1000)


if __name__ == '__main__' :
    wallet = []
    wallet.append(CreditCard('John Bowman','California Savings',
                             '5391 0375 9387 5309' , 2500))
    wallet.append(CreditCard('John Bowman','California Federal',
                             '3485 0399 3395 1954' , 3500))
    wallet.append(CreditCard('John Bowman','California Finance',
                             '5391 0375 9387 5309' , 5000))
    
    for val in range(1,17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)
        
    for c in range(3):
        print('Customer = ', wallet[c].get_customer())
        print('Bank = ', wallet[c].get_bank())
        print('Account = ', wallet[c].get_account())
        print('Limit = ', wallet[c].get_limit())
        print('Balance = ', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New balance = ', wallet[c].get_balance())
        print()
        

w = CreditCard('John Delaney','World Bank','5003 4005 5892 7101',10000)
print (w.get_customer())
print (w.get_bank())
print (w.get_account())
print (w.get_limit())
print (w.get_balance())
print (w.charge(5000))
print (w.get_balance())
print (w.make_payment(1400))
print (w.make_payment('hey'))


# In[8]:

# R-2.6

class CreditCard():
    
    """A Consumer Credit Card"""
    
    def __init__(self,customer,bank,acct,limit):
        """
        Create a new Credit Card Instance
        
        The initial balance is Zero
        customer - the name of the customer (e.g., John Bowman )
        bank - the name of the bank (e.g., California Savings )
        acnt - the acount identifier (e.g., 5391 0375 9387 5309 )
        limit credit limit (measured in dollars)
        
        """
        self._customer = customer
        self._bank = bank
        self._account = acct
        self._limit = limit
        self._balance = 0
         
    def get_customer(self):
        
        """get the name of the customer"""
        
        return (self._customer)
    
    def get_bank(self):
        
        """Returns the bank's name"""
        
        return (self._bank)
    
    def get_account(self):
        
        """Returns the card identifying number (String)"""
        
        return (self._account)
    
    def get_limit(self):
        
        """Returns the current credit limit"""
        
        return (self._limit)
    
    def get_balance(self):
        
        """Returns the current balance"""
        
        return (self._balance)
    
    def charge(self,price):
        
        """
        Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed; False if charge was denied.
        
        """
        if price + self._balance > self._limit:
            return False
        else:
            self._balance+=price
            return True
        
    def make_payment(self,amount):
        
        """
        Makes payment that reduces balance
        """
        if (amount<0):
            raise ValueError('Negative values are not accepted')
            
        self._balance = self._balance-amount
        return self._balance
        
        
cc = CreditCard('John Doe', '1st Bank' , '5391 0375 9387 5309' , 1000)


if __name__ == '__main__' :
    wallet = []
    wallet.append(CreditCard('John Bowman','California Savings',
                             '5391 0375 9387 5309' , 2500))
    wallet.append(CreditCard('John Bowman','California Federal',
                             '3485 0399 3395 1954' , 3500))
    wallet.append(CreditCard('John Bowman','California Finance',
                             '5391 0375 9387 5309' , 5000))
    
    for val in range(1,17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)
        
    for c in range(3):
        print('Customer = ', wallet[c].get_customer())
        print('Bank = ', wallet[c].get_bank())
        print('Account = ', wallet[c].get_account())
        print('Limit = ', wallet[c].get_limit())
        print('Balance = ', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New balance = ', wallet[c].get_balance())
        print()
        

w = CreditCard('John Delaney','World Bank','5003 4005 5892 7101',10000)
print (w.get_customer())
print (w.get_bank())
print (w.get_account())
print (w.get_limit())
print (w.get_balance())
print (w.charge(5000))
print (w.get_balance())
print (w.make_payment(1400))
print (w.make_payment(-3789))


# In[16]:

# R-2.7

from Code_Fragment_Examples import CreditCard


# In[20]:

class SecondaryCreditCard(CreditCard):
    """Defining a new credit card account class with non zero balance"""
    
    def __init__(self,customer,bank,acct,limit,balance):
        
        """Initial constructor receiving fifth paramter - balance"""
        
        super().__init__(customer,bank,acct,limit)
        self._balance=balance
    
    def get_balance_amount(self):
        return (self._balance)
    
sec_credit_card = SecondaryCreditCard('John','Local Bank','4059 8939 3993 3992',9000,2000)
print (sec_credit_card.get_balance_amount())
print (sec_credit_card.get_customer())
print (sec_credit_card.get_bank())
print (sec_credit_card.get_account())
print (sec_credit_card.get_limit())


# In[5]:

# R-2.8

class CreditCard():
    
    """A Consumer Credit Card"""
    
    def __init__(self,customer,bank,acct,limit):
        """
        Create a new Credit Card Instance
        
        The initial balance is Zero
        customer - the name of the customer (e.g., John Bowman )
        bank - the name of the bank (e.g., California Savings )
        acnt - the acount identifier (e.g., 5391 0375 9387 5309 )
        limit credit limit (measured in dollars)
        
        """
        self._customer = customer
        self._bank = bank
        self._account = acct
        self._limit = limit
        self._balance = 0
         
    def get_customer(self):
        
        """get the name of the customer"""
        
        return (self._customer)
    
    def get_bank(self):
        
        """Returns the bank's name"""
        
        return (self._bank)
    
    def get_account(self):
        
        """Returns the card identifying number (String)"""
        
        return (self._account)
    
    def get_limit(self):
        
        """Returns the current credit limit"""
        
        return (self._limit)
    
    def get_balance(self):
        
        """Returns the current balance"""
        
        return (self._balance)
    
    def charge(self,price):
        
        """
        Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed; False if charge was denied.
        
        """
        if price + self._balance > self._limit:
            return False
        else:
            self._balance+=price
            return True
        
    def make_payment(self,amount):
        
        """
        Makes payment that reduces balance
        """
        
        self._balance = self._balance-amount
        
        
cc = CreditCard('John Doe', '1st Bank' , '5391 0375 9387 5309' , 1000)


if __name__ == '__main__' :
    wallet = []
    wallet.append(CreditCard('John Bowman','California Savings',
                             '5391 0375 9387 5309' , 2500))
    wallet.append(CreditCard('John Bowman','California Federal',
                             '3485 0399 3395 1954' , 3500))
    wallet.append(CreditCard('John Bowman','California Finance',
                             '5391 0375 9387 5309' , 5000))
    
    for val in range(1,25):
        print (wallet[0].charge(10*val),'California_Savings')
        print (wallet[1].charge(10*val),'California_Federal')
        print (wallet[2].charge(10*val),'California_Finance')
        
    for c in range(3):
        print('Customer = ', wallet[c].get_customer())
        print('Bank = ', wallet[c].get_bank())
        print('Account = ', wallet[c].get_account())
        print('Limit = ', wallet[c].get_limit())
        print('Balance = ', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New balance = ', wallet[c].get_balance())
        print()


# + The Credit card that would go over the credit limit sooner eventually would be **California Savings** Credit Card, as demonstrated the last three iterations of california savings is shown to be `False` when `i=22`,`i=23` and `i=24`. 
# + The Range is changed from `range(1,17)` to `range(1,25)` and the factors are increased to `10`.

# In[9]:

# R-2.9

class Vector():
    """Represent a Vector in Multi-Dimensional Space"""
    
    def __init__(self,d):
        """Initializes a d-dimensional vector"""
        self._coords = [0]*d
        
    def __len__(self):
        """Returns the dimension of the vector"""
        return (len(self._coords))
    
    def __getitem__(self,j):
        """Returns the jth co-ordinate of a vector"""
        return (self._coords[j])
    
    def __setitem__(self,j,val):
        """Assigns a value to jth location of a vector"""
        self._coords[j] = val
        
    def __add__(self,other):
        """Returns the sum of two vectors"""
        
        if (len(other)!=len(self)):
            raise ValueError("dimensions must match")
        result = Vector(len(self))
        for g in range(len(self)):
            result[g] = other[g] + self[g]
        return result
    
    def __sub__(self,other):
        """
        Returns the difference of two vectors
        """
        if (len(other)!=len(self)):
            raise ValueError("dimensions must match")
        result_diff = Vector(len(self))
        for g in range(len(self)):
            result_diff[g] = other[g] - self[g]
        return (result_diff.__str__())
    
    def __eq__(self,other):
        """Returns the boolean value if equal/not equal"""
        return (self._coords==other._coords)
    
    def __ne__(self,other):
        """Return True if Vector differs from Other"""
        return not self==other
    
    def __str__(self):
        """Returns the string Representation"""
        return ('<' + str(self._coords)[1:-1] + '>')
    

u = Vector(5)
u.__setitem__(3,41)
u.__setitem__(2,31)
u.__setitem__(4,10)
print (u.__str__())
print (u.__sub__([7,1,23,2,1]))


# In[11]:

# R-2.10

class Vector():
    """Represent a Vector in Multi-Dimensional Space"""
    
    def __init__(self,d):
        """Initializes a d-dimensional vector"""
        self._coords = [0]*d
        
    def __len__(self):
        """Returns the dimension of the vector"""
        return (len(self._coords))
    
    def __getitem__(self,j):
        """Returns the jth co-ordinate of a vector"""
        return (self._coords[j])
    
    def __setitem__(self,j,val):
        """Assigns a value to jth location of a vector"""
        self._coords[j] = val
        
    def __add__(self,other):
        """Returns the sum of two vectors"""
        
        if (len(other)!=len(self)):
            raise ValueError("dimensions must match")
        result = Vector(len(self))
        for g in range(len(self)):
            result[g] = other[g] + self[g]
        return result
    
    def __eq__(self,other):
        """Returns the boolean value if equal/not equal"""
        return (self._coords==other._coords)
    
    def __ne__(self,other):
        """Return True if Vector differs from Other"""
        return not self==other
    
    def __neg__(self):
        """Returns the negative of given vector"""
        neg_vector = Vector(len(self))
        for g in range(len(self)):
            neg_vector[g] = -1*self[g]
        return (neg_vector.__str__())
    
    def __str__(self):
        """Returns the string Representation"""
        return ('<' + str(self._coords)[1:-1] + '>')
    
    
v = Vector(10)
print (v)
v.__setitem__(4,8)
v.__setitem__(3,87)
v.__setitem__(5,10)
v.__setitem__(1,53)
print (v)
print (v.__neg__())


# In[16]:

# R-2.11

class Vector():
    """Represent a Vector in Multi-Dimensional Space"""
    
    def __init__(self,d):
        """Initializes a d-dimensional vector"""
        self._coords = [0]*d
        
    def __len__(self):
        """Returns the dimension of the vector"""
        return (len(self._coords))
    
    def __getitem__(self,j):
        """Returns the jth co-ordinate of a vector"""
        return (self._coords[j])
    
    def __setitem__(self,j,val):
        """Assigns a value to jth location of a vector"""
        self._coords[j] = val
        
    def __add__(self,other):
        """Returns the sum of two vectors"""
        
        if (len(other)!=len(self)):
            raise ValueError("dimensions must match")
        
        result = Vector(len(self))
        if isinstance(other,(list,tuple)):
            other_vector = Vector(len(other))
            for h in range(len(other)):
                other_vector[h]=other[h]
        elif (isinstance(other,Vector)):
            other_vector=other
            
        for g in range(len(self)):
            result[g] = other_vector[g] + self[g]
        return result.__str__()
    
    def __eq__(self,other):
        """Returns the boolean value if equal/not equal"""
        return (self._coords==other._coords)
    
    def __ne__(self,other):
        """Return True if Vector differs from Other"""
        return not self==other
    
    def __str__(self):
        """Returns the string Representation"""
        return ('<' + str(self._coords)[1:-1] + '>')
    

r = Vector(5)
r.__setitem__(2,10)
r.__setitem__(1,16)
r.__setitem__(3,9)
print (r.__str__())
print (r.__add__([4,1,0,8,21]))

s= Vector(5)
s.__setitem__(4,20)
s.__setitem__(2,-4)
s.__setitem__(1,-5)
print (s.__str__())

print (r.__str__())
print (r.__add__(s))


# + To handle `v = u + [5,3,10,-2,1]` and `v = [5,3,10,-2,1] + u`, It is recommended to have both `u` and `[5,3,10,-2,1]` to be of same data type, that way it can handle both scenarios

# In[17]:

# R-2.12

class Vector():
    """Represent a Vector in Multi-Dimensional Space"""
    
    def __init__(self,d):
        """Initializes a d-dimensional vector"""
        self._coords = [0]*d
        
    def __len__(self):
        """Returns the dimension of the vector"""
        return (len(self._coords))
    
    def __getitem__(self,j):
        """Returns the jth co-ordinate of a vector"""
        return (self._coords[j])
    
    def __setitem__(self,j,val):
        """Assigns a value to jth location of a vector"""
        self._coords[j] = val
        
    def __add__(self,other):
        """Returns the sum of two vectors"""
        
        if (len(other)!=len(self)):
            raise ValueError("dimensions must match")
        result = Vector(len(self))
        for g in range(len(self)):
            result[g] = other[g] + self[g]
        return result
    
    def __mul__(self,m):
        """Returns the Vector after multiplying the original Vector with m"""
        result_mul = Vector(len(self))
        for g in range(len(self)):
            result_mul[g] = self[g]*m
        return (result_mul.__str__())

    def __eq__(self,other):
        """Returns the boolean value if equal/not equal"""
        return (self._coords==other._coords)
    
    def __ne__(self,other):
        """Return True if Vector differs from Other"""
        return not self==other
    
    def __str__(self):
        """Returns the string Representation"""
        return ('<' + str(self._coords)[1:-1] + '>')
    
    
r = Vector(5)
r.__setitem__(2,10)
r.__setitem__(1,16)
r.__setitem__(3,9)
print (r.__str__())
print (r.__mul__(3))
print (r.__mul__(10))


# ##### R-2.13
# 
# + Similar to the problem - 2.11, Implement the convergence of both the input formats to the same result as `v*3 ==3*v`

# In[1]:

# R-2.14

class Vector():
    """Represent a Vector in Multi-Dimensional Space"""
    
    def __init__(self,d):
        """Initializes a d-dimensional vector"""
        self._coords = [0]*d
        
    def __len__(self):
        """Returns the dimension of the vector"""
        return (len(self._coords))
    
    def __getitem__(self,j):
        """Returns the jth co-ordinate of a vector"""
        return (self._coords[j])
    
    def __setitem__(self,j,val):
        """Assigns a value to jth location of a vector"""
        self._coords[j] = val
        
    def __add__(self,other):
        """Returns the sum of two vectors"""
        
        if (len(other)!=len(self)):
            raise ValueError("dimensions must match")
        result = Vector(len(self))
        for g in range(len(self)):
            result[g] = other[g] + self[g]
        return result
    
    def dot_product(self,other):
        """Returns the dot product of two vectors"""
        if (len(other)!=len(self)):
            raise ValueError("dimensions must match")
        scalar_product=0
        for g in range(len(self)):
            scalar_product+=other[g]*self[g]
        return scalar_product
    
    def __eq__(self,other):
        """Returns the boolean value if equal/not equal"""
        return (self._coords==other._coords)
    
    def __ne__(self,other):
        """Return True if Vector differs from Other"""
        return not self==other
    
    def __str__(self):
        """Returns the string Representation"""
        return ('<' + str(self._coords)[1:-1] + '>')
    

r = Vector(5)
r.__setitem__(2,10)
r.__setitem__(1,16)
r.__setitem__(3,9)
r.__setitem__(4,19)
r.__setitem__(0,1)
print (r.__str__())

s = [4,1,7,2,8]
print (s)
print (r.dot_product(s))


# In[2]:

# R-2.15

class Vector():
    """Represent a Vector in Multi-Dimensional Space"""
    
    def __init__(self,d):
        """Initializes a d-dimensional vector"""
        if isinstance(d,int):
            self._coords = [0]*d
        elif(isinstance(d,(list,tuple))):
            vector=Vector(len(d))
            for h in range(len(d)):
                vector[h]=d[h]
            self._coords=vector
        
    def __len__(self):
        """Returns the dimension of the vector"""
        return (len(self._coords))
    
    def __getitem__(self,j):
        """Returns the jth co-ordinate of a vector"""
        return (self._coords[j])
    
    def __setitem__(self,j,val):
        """Assigns a value to jth location of a vector"""
        self._coords[j] = val
        
    def __add__(self,other):
        """Returns the sum of two vectors"""
        
        if (len(other)!=len(self)):
            raise ValueError("dimensions must match")
        result = Vector(len(self))
        for g in range(len(self)):
            result[g] = other[g] + self[g]
        return result
    
    def __eq__(self,other):
        """Returns the boolean value if equal/not equal"""
        return (self._coords==other._coords)
    
    def __ne__(self,other):
        """Return True if Vector differs from Other"""
        return not self==other
    
    def __str__(self):
        """Returns the string Representation"""
        return ('<' + str(self._coords)[1:-1] + '>')
    
    
r = Vector(5)
r.__setitem__(2,10)
r.__setitem__(1,16)
r.__setitem__(3,9)
r.__setitem__(4,19)
r.__setitem__(0,1)
print (r.__str__())

q = list(range(5))
c = Vector(q)
print (c.__str__())


# ###### R-2.16
# 
# + In Arithmetic progression assume `a=start`,`b=stop`,`d=step`.Range function has three arguments - `range(start,stop,step)`. The nth term of the progression is defined as `b=a+(n-1)*d`.
# + Now, from above equation calculate `n` which is `(b-a+d)/d`.
# + As we now the terms in the sequence of `range(start,stop,step)` start from `start` and end with `stop-1` and is 0-indexed, the `b` is replaced with `b-1` to be precise about the number of terms 
# + As a result, `n=(b-a+d-1)/d` is justified where `b=stop`,`a=start`,`d=step`.

# In[6]:

# R-2.18

from Progression_Example import Progression
from Fibonacci_Series import Fibonacci_Series

fib_series = Fibonacci_Series(2,2)
fib_series.advance()
fib_series.advance()
fib_series.advance()
fib_series.advance()
fib_series.advance()
fib_series.advance()
fib_series.advance()
fib_series.advance()
fib_series.advance()
fib_series.advance()
fib_series.advance()
FibSeries = fib_series.__getitem__()
FibSeries[0]=2
print (FibSeries)
print (FibSeries[7])


# In[ ]:

# R-2.19

from ArithmeticProgression import *
arithmetic_progression = ArithmeticProgression(128,0)
C=0
obj = arithmetic_progression._current
while (obj <= 2**63):
    C+=1
    obj=arithmetic_progression.advance()
    
print (C) ## Via Code 

"""
Using Arithmetic progression b = a + (n-1)*d
we get 2**63 >= 0 + (n-1)*(2**7)

Find the value of n which is n <= (2**56)+1

"""


# ##### R-2.20
# 
# The few efficiency drawbacks of having large and deeper trees is that:
#     
#     The only efficiency problems for a deep inheritance tree that I can see is that super may be called many times over in a deep inheritance tree when calling the constructor for the deepest class.
# 
#     Also, if there is a method signature that is overridden in each class, the compiler will take longer to sort out or determine which method is overridden.
#     
# Find more clear explanations [here](https://stackoverflow.com/questions/28721913/efficiency-disadvantages-of-having-very-deep-and-very-shallow-inheritance-trees)
# 

# ##### R-2.21
# 
# Again the more detailed explanations can be found [here](https://stackoverflow.com/questions/28721913/efficiency-disadvantages-of-having-very-deep-and-very-shallow-inheritance-trees)

# In[ ]:

#R-2.22

from abc import ABCMeta, abstractmethod

class Sequence(metaclass=ABCMeta):
    """
    Our own version of collections.Sequence 
    abstract base class
    """
    @abstractmethod
    def __len__(self):
        """
        Returns the length of the sequence
        """
    @abstractmethod
    def __getitem__(self):
        """
        Returns the element at index j of the sequence
        """
    def __contains__(self,val):
        """
        Returns True if val is found in the sequence, False Otherwise
        """
        for j in range(len(self)):
            if self[j]==val:
                return True
        return False
        
    def index(self,val):
        """
        Return leftmost index at which val is found (or raise ValueError)
        """
        for j in range(len(self)):
            if self[j]==val:
                return (j)
        raise ValueError('value not in sequence')
        
    
    def __eq__(self,seq):
        """
        Returns Boolean indicator if every element of the sequence is equal to respective element of the
        original sequence
        """
        if (len(self)!=len(seq)):
            raise ValueError('The dimension must match')
        bools=[]
        if len(self)==len(seq):
            for g in range(len(self)):
                if (self[g]==seq[g]):
                    bools.append(self[g]==seq[g])
        x = len(list(set(bools)))
        y = len(bools)
        if (x==y==1 and bools[0]==True):
            return True
        else:
            return False
        
        
    def count(self,val):
        """
        Returns the number of elements equal to given value
        """
        C=0
        for j in range(len(self)):
            if (self[j]==val):
                C+=1
        return C


# In[ ]:

# R-2.23

from abc import ABCMeta, abstractmethod

class Sequence(metaclass=ABCMeta):
    """
    Our own version of collections.Sequence 
    abstract base class
    """
    @abstractmethod
    def __len__(self):
        """
        Returns the length of the sequence
        """
    @abstractmethod
    def __getitem__(self):
        """
        Returns the element at index j of the sequence
        """
    def __contains__(self,val):
        """
        Returns True if val is found in the sequence, False Otherwise
        """
        for j in range(len(self)):
            if self[j]==val:
                return True
        return False
        
    def index(self,val):
        """
        Return leftmost index at which val is found (or raise ValueError)
        """
        for j in range(len(self)):
            if self[j]==val:
                return (j)
        raise ValueError('value not in sequence')
        
    def __it__(self,seq):
        """Lexigographic Comparison"""
        
        if (len(self)!=len(seq)):
            raise ValueError('The dimension must match')
        lex_bools = []
        if (len(self)==len(seq)):
            for h in range(len(self)):
                if (self[h]<seq[h]):
                    lex_bools.append(self[h]<seq[h])
        w = len(list(set(lex_bools)))
        v = len(lex_bools)
        if (w==v==1 and lex_bools[0]==True):
            print ('Seq1<Seq2')
        elif (w==v==1 and lex_bools[0]==False):
            print ('Seq1>Seq2')
        
    
    def count(self,val):
        """
        Returns the number of elements equal to given value
        """
        C=0
        for j in range(len(self)):
            if (self[j]==val):
                C+=1
        return C

