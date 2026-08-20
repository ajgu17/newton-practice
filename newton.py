import numpy as np
import numdifftools as nd

def newton_optimize_with_packages(f, x0, tol=1e-6, max_iter=100):
    """
    Newton's method of optimization for multivariate function. 
    """
    x = np.array(x0, dtype=float)
    
    # Define external package tools for gradient and Hessian
    grad_func = nd.Gradient(f)
    hess_func = nd.Hessian(f)
    
    for i in range(max_iter):
        # Package computes finite differences automatically under the hood
        g = grad_func(x)
        H = hess_func(x)
        
        grad_norm = np.linalg.norm(g)
        if grad_norm < tol:
            print(f"Converged in {i} iterations.")
            return x
            
        try:
            # Solve H * step = g
            step = np.linalg.solve(H, g)
            x -= step
        except np.linalg.LinAlgError:
            print("Hessian is singular. Optimization failed.")
            return None
            
    print("Reached maximum iterations.")
    return x

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

    