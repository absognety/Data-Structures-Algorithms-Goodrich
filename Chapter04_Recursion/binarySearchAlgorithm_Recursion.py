def binary_search(data,target,low,high):
    #low < high (no interval) -- returns False
    if low > high:
        return False
    else:
        #calculate the mid value based on low and high
        mid = (low + high)//2
        if target == data[mid]: #if desired value median of original List
            return (mid,target)
        elif target < data[mid]:
            # recur on the portion left of the middle
            binary_search(data,target,low,mid-1)
        else:
            # recur on the portion right of the middle
            binary_search(data,target,mid+1,high)
            
#Code Fragment 4.3: An implementation of the binary search algorithm.