arr = list(map(int,input().strip().split()))

def reverseArray(arr,start,stop):
    l = len(arr)
    if (l==0 | l==1):
        return arr
    else:
        if start < stop-1:
            arr[start],arr[stop-1] = arr[stop-1],arr[start]
            reverseArray(arr,start+1,stop-1)
        return (arr)
    
#Code Fragment 4.10: Reversing the elements of a sequence using linear recursion.