import math

def derivative(x,f):
    epsilon = 0.001
    return (f(x+epsilon)-f(x))/epsilon

def optimize(x, f):
    epsilon = 0.001
    d=2
    while d>0.001:
        d=derivative(x,f)/(derivative(x+epsilon,f)-derivative(x,f))*epsilon
        y=x-d
        x=y
    return y,f(y)