
def derivative(x,f):
    """Compute derivative using finite different with epsilon = 0.001 of f at x"""
    epsilon = 0.0001
    return (f(x+epsilon)-f(x))/epsilon

def optimize(x, f):
    """Find the minimum of f starting from x"""
    epsilon = 0.0001
    d=2
    while abs(d)>0.001:
        d=derivative(x,f)/(derivative(x+epsilon,f)-derivative(x,f))*epsilon
        y=x-d
        x=y
    return y,f(y)