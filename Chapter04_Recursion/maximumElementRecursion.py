arr = list(map(int,input().strip().split()))

C = 0
reqMax = arr[0]
stop = len(arr)-1
def findMaxRecursion(arr,C,reqMax):
    start = 0
    #print(C)
    print (reqMax)
    if C == stop:
        return (reqMax)
    else:
        reqMax = max(reqMax,arr[start])
        C += 1
        findMaxRecursion(arr[start+1:],C,reqMax)
        
findMaxRecursion(arr,C,reqMax)
#finding the maximum element in a list using recursion