from Progression_Example import Progression

class GeometricProgression(Progression): #inherit from progression
    """
    Iterator producing Geometric Progression
    
    """
    def __init__(self,base=2,start=1):
        """
        Create a new Geometric Progression
        base: A common ratio to be multiplied to each term(default 2)
        start: Starting term (default 1)
        """
        super().__init__(start)
        self._base = base
        
    def advance(self): #override inherited version
        """
        Update Current Value by multiplying it with base value
        """
        self._current*=self._base
        
#WCode Fragment 2.10: A class that produces a geometric progression