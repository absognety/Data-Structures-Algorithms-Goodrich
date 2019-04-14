arr = list(map(int,input().strip().split()))

def getSum(array):
    l = len(array)
    result=0
    if l==0:
        return 0
    else:
        result = getSum(array[:l-1]) + array[l-1]
    return (result)

print (getSum(arr))

#Code Fragment 4.9: Summing the elements of a sequence using linear recursion