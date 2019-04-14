def power(x,n):
    """
    Compute the value of x raised to power n
    """
    if n==0:
        return (1)
    else:
        return (x * power(x,n-1))
    
#Code Fragment 4.11: Computing the power function using trivial recursion.