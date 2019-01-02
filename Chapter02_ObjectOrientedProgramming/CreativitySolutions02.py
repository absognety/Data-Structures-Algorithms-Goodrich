
# coding: utf-8

# #### Creativity Solutions
# 
# ###### C-2.24-2.32

# In[5]:

# C-2.25

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
    
    def __mul__(self,entity):
        """
        Runtime check if entity is a vector or a scalar
        """
        product=0
        result_mul=[0]*len(self)
        if isinstance(entity,Vector):
            if (len(entity)!=len(self)):
                raise ValueError('The dimension must match')
            else:
                for g in range(len(self)):
                    product+=(self.__getitem__(g)*entity.__getitem__(g))
            return (product)
        
        elif(isinstance(entity,(int,float))):
            for h in range(len(self)):
                result_mul[h]=self[h]*entity
            return (result_mul)
    
    def __eq__(self,other):
        """Returns the boolean value if equal/not equal"""
        return (self._coords==other._coords)
    
    def __ne__(self,other):
        """Return True if Vector differs from Other"""
        return not self==other
    
    def __str__(self):
        """Returns the string Representation"""
        return ('<' + str(self._coords)[1:-1] + '>')
    
X = Vector(5)
X.__setitem__(0,34)
X.__setitem__(1,89)
X.__setitem__(4,21)
X.__setitem__(3,41)
print (X.__str__())
Y = Vector(5)
Y.__setitem__(2,19)
Y.__setitem__(1,32)
Y.__setitem__(3,38)
Y.__setitem__(4,10)
print (Y.__str__())

print (Y.__mul__(X))

print (X.__mul__(10))
print (Y.__mul__(10))


# In[6]:

# C-2.26

class ReversedSequenceIterator():
    """An iterator for any of Python's sequence types."""
    
    def __init__(self,sequence):
        """Create an iterator for the given sequence."""
        self._seq = sequence[::-1] # keep a reference to the underlying data
        self._k = -1 # will increment to 0 on first call to next
        
    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        self._k += 1 # advance to next index
        if self._k < len(self._seq):
            return(self._seq[self._k]) # return the data element
        else:
            raise StopIteration() # there are no more elements
            
    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self
    
V = ReversedSequenceIterator([1,8,3,6,10,5,12])
print (V.__next__())
print (V.__next__())
print (V.__next__())
print (V.__next__())
print (V.__next__())


# In[14]:

# C-2.27

class Range():
    
    """
    Class that mimics the built-in range class
    
    """
    def __init__(self,start=0,stop=None,step=1):
        
        
        if (step==0):
           raise ValueError('Step cannot be Zero')
           
        if stop is None:
            start,stop=0,start
           
        self._length = max(0,(stop-start+step-1)//step)
       
        # need knowledge of start and step to support getitem
        self._start=start
        self._step=step
        self._stop=stop
    
    def __len__(self):
        return (self._length)
    
    def __contains_(self,H):
        if self._step==1:
            if self._start<=H<self._stop:
                return True
            else:
                return False
        else:
            if (self._start<=H<self._stop):
                if ((H-self._start)%(self._step) == 0):
                    return True
                else:
                    return False
    
    def __getitem__(self,k):
        
        if (k < 0):
            k += self._length
            
        if not 0<=k<self._length:
            raise IndexError('Index out of range')
            
        return (self._start+(k*self._step))
      
        
D = Range(27)
print (20 in D)
print (19 in D)
print (10 in D)
print (27 in D)
print (28 in D)

print ('\n')
E = Range(27,190,4)
print (30 in E)
print (187 in E)
print (31 in E)
print (27 in E)
print (173 in E)
print (67 in E)
print (103 in E)


# In[ ]:

# C-2.28

from Code_Fragment_Examples import CreditCard


class PredatoryCreditCard(CreditCard):
    
    def __init__(self,customer,bank,acct,limit,apr):
        """
        Create a new predatory credit card instance.

        The initial balance is zero.
        
        customer the name of the customer (e.g., John Bowman )
        bank the name of the bank (e.g., California Savings )
        acnt the acount identifier (e.g., 5391 0375 9387 5309 )
        limit credit limit (measured in dollars)
        apr annual percentage rate (e.g., 0.0825 for 8.25% APR)
        
        """
        super().__init__(customer,bank,acct,limit)
        self._apr=apr
        self.count_charge=0
        
    def charge(self,price):
        """
        Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed.
        Return False and assess 5 fee if charge is denied.
        
        """
        self.count_charge+=1
        success = super().charge(price) #call inherited value
        if not success:
            self._balance+=5            #assess penalty
        if (self.count_charge>10):
            self.additional_charge()    #additional penalty of $1 for beyond 10 calls to charge
        return success                  #caller expects value
    
    def process_month(self):
        """
        Assess monthly interest on outstanding balance.
        
        """
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance*=monthly_factor
        return (self._balance)
    
    def additional_charge(self):
        """
        Additional charge of $1 for every additional call
        made to function charge beyond 10 calls
        """
        self._balance=self._balance+1
            
#Code Fragment 2.7: A subclass of CreditCard that assesses interest and fees.


# In[ ]:

# C-2.29

from Code_Fragment_Examples import CreditCard


class PredatoryCreditCard(CreditCard):
    
    def __init__(self,customer,bank,acct,limit,apr):
        """
        Create a new predatory credit card instance.

        The initial balance is zero.
        
        customer the name of the customer (e.g., John Bowman )
        bank the name of the bank (e.g., California Savings )
        acnt the acount identifier (e.g., 5391 0375 9387 5309 )
        limit credit limit (measured in dollars)
        apr annual percentage rate (e.g., 0.0825 for 8.25% APR)
        
        """
        super().__init__(customer,bank,acct,limit)
        self._apr=apr
        
    def charge(self,price):
        """
        Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed.
        Return False and assess 5 fee if charge is denied.
        
        """
        success = super().charge(price) #call inherited value
        if not success:
            self._balance+=5            #assess penalty
        return success                  #caller expects value
    
    def process_month(self):
        """
        Assess monthly interest on outstanding balance.
        
        """
        process_month_ind=True
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance = self._balance + (self._balance*monthly_factor)
        return (self._balance,monthly_factor,process_month_ind)
    
    def late_fees(self,Fee):
        
        """
        Late Fees will be charged if customer fails to 
        pay the minimum monthly payment assigned to him/her
        """
        final_balance,monthlyFactor,Ind = self.process_month()
        if Ind:
            if (self._balance > 0):
                if (self._balance!=final_balance):
                    self._balance = self._balance + (self._balance*monthlyFactor) + Fee
        return (self._balance)
            
#Code Fragment 2.7: A subclass of CreditCard that assesses interest and fees.


# In[ ]:

# C-2.30

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
        
    def _set_balance(self):
        
        """
        A function to Change the  balance and manipulate it
        
        """
        #Write your Function here to play with 'balance' parameter......
        pass
         
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
        
class PredatoryCreditCard(CreditCard):
    
    def __init__(self,customer,bank,acct,limit,apr):
        """
        Create a new predatory credit card instance.

        The initial balance is zero.
        
        customer the name of the customer (e.g., John Bowman )
        bank the name of the bank (e.g., California Savings )
        acnt the acount identifier (e.g., 5391 0375 9387 5309 )
        limit credit limit (measured in dollars)
        apr annual percentage rate (e.g., 0.0825 for 8.25% APR)
        
        """
        super().__init__(customer,bank,acct,limit)
        self._apr=apr
        super()._set_balance()
        
    def charge(self,price):
        """
        Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed.
        Return False and assess 5 fee if charge is denied.
        
        """
        success = super().charge(price) #call inherited value
        if not success:
            self._balance+=5            #assess penalty
        return success                  #caller expects value
    
    def process_month(self):
        """
        Assess monthly interest on outstanding balance.
        
        """
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance*=monthly_factor
        return (self._balance)
            
#Code Fragment 2.7: A subclass of CreditCard that assesses interest and fees.
#CreditCard and PredatoryCreditCard are changed accordingly 


# In[5]:

# C-2.31

from Progression_Example import Progression

class SpecialFibonacciSeries(Progression):
    """
    Iterator producing a generalized Fibonacci progression.
    """
    
    def __init__(self, first=2, second=200):
        """
        Create a new fibonacci progression.
        first the first term of the progression (default 0)
        second the second term of the progression (default 1)
        """
        super().__init__(second) # start progression at first
        self._prev = first # fictitious value preceding the first
        self._series = []
        
    def advance(self):
        """
        Update current value by taking sum of previous two.
        """
        self._prev, self._current = self._current, abs(self._prev - self._current)
        self._series.append(self._current)
                    
    def __getitem__(self):
        return ([2,200] + self._series)
        
        
special_series = SpecialFibonacciSeries()
special_series.advance()
special_series.advance()
special_series.advance()
special_series.advance()
special_series.advance()
special_series.advance()
special_series.advance()
special_series.advance()
special_series.advance()
special_series.advance()
special_series.advance()
special_series.advance()
special_series.advance()
special_series.advance()
special_series.advance()
print (special_series.__getitem__())


# In[7]:

# C-2.32

import math

from Progression_Example import Progression

class SpecialSeries(Progression):
    """
    Iterator producing a generalized Fibonacci progression.
    """
    
    def __init__(self, first=65536):
        """
        Create a new fibonacci progression.
        first the first term of the progression (default 0)
        second the second term of the progression (default 1)
        """
        super().__init__(first)
        self._series=[]
        
    def advance(self):
        """
        Update current value by taking sum of previous two.
        """
        self._current = math.sqrt(self._current)
        self._series.append(self._current)
                    
    def __getitem__(self):
        return ([65536] + self._series)
        
        
series = SpecialSeries()
series.advance()
series.advance()
series.advance()
series.advance()
series.advance()
series.advance()
series.advance()
series.advance()
series.advance()
series.advance()
series.advance()
print (series.__getitem__())

