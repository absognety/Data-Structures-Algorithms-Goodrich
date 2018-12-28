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
    
    def count(self,val):
        """
        Returns the number of elements equal to given value
        """
        C=0
        for j in range(len(self)):
            if (self[j]==val):
                C+=1
        return C
    