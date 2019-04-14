def binary_sum(S,start,stop):
    """
    Return the sum of the numbers in implicit slice S[start:stop].
    """
    if start >= stop:                  # zero elements in slice
        return (0)
    elif start == stop-1:              # One element in slice
        return (S[start])
    else:                              # two or more elements in slice
        mid = (start + stop)//2
        return (binary_sum(S,start,mid) + binary_sum(S,mid,stop))
                
#Code Fragment 4.13: Summing the elements of a sequence using binary recursion.