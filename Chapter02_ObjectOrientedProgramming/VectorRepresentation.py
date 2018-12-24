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
    
    def __str__(self):
        """Returns the string Representation"""
        return ('<' + str(self._coords)[1:-1] + '>')
    
    