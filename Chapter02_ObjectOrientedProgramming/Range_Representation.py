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
       
        # need knowledge of start and step (but not stop) to support getitem
        self._start=start
        self._step=step
    
    def __len__(self):
        return (self._length)
    
    def __getitem__(self,k):
        
        if (k < 0):
            k += self._length
            
        if not 0<=k<self._length:
            raise IndexError('Index out of range')
            
        return (self._start+(k*self._step))
      
       
       