def reverse_iterative(data):
    """
    Reverse elements in data - S
    """
    start,stop = 0,len(data)
    while start < stop-1:
        data[start],data[stop-1] = data[stop-1],data[start] #Swap first and last
        start,stop = start + 1, stop - 1                    #narrow and range
        
#Code Fragment 4.16: Reversing the elements of a sequence using iteration
