from Progression_Example import Progression

class ArithmeticProgression(Progression): #inherit the progression
    """
    Iterator producing an arithmetic progression.
    """
    
    def init (self, increment=1, start=0):
        """
        Create a new arithmetic progression.
        increment the fixed constant to add to each term (default 1)
        start the first term of the progression (default 0)
        """
        super().__init__(start) # initialize base class
        self._increment = increment
        
        def advance(self): # override inherited version
            """
            Update current value by adding the fixed increment.
            """
            self._current += self._increment

#Code Fragment 2.9: A class that produces an arithmetic progression