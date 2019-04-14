
def power(x,n):
    """
    Compute the power function using repeated squaring
    """
    if n==0:
        return (1)
    else:
        partial = power(x,n//2)          # rely on truncated division
        result = partial * partial
        if n%2==1:
            result = result * x          #if n odd, include extra factor of x
        return (result)
    
#Code Fragment 4.12: Computing the power function using repeated squaring