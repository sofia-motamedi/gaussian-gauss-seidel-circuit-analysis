# Gauss-Seidel Iterative Method

from numpy import array, zeros, dot, linalg

# Define the coefficient matrix (a) and constant vector (b):
a = array([[6, -4, 0],
           [-4, 9, -2],
           [0, -2, 7]], float)
b = array([10, 5, 8], float)
n = len(b)

def gauss_seidel(a, b, tol=1e-9, max_iter=100):
    n = len(b)
    x = zeros(n, float)
    
    for iteration in range(max_iter):
        x_old = x.copy()
        
        # Update each variable sequentially
        for i in range(n):
            # For j < i, we use the updated (new) values from the current iteration.
            # For j > i, we use the values from the previous iteration.
            sum_before = 0
            for j in range(i):
                sum_before += a[i, j] * x[j]
            sum_after = 0
            for j in range(i + 1, n):
                sum_after += a[i, j] * x_old[j]
            
            # Update x[i] using the Gauss-Seidel formula:
            x[i] = (b[i] - sum_before - sum_after) / a[i, i]
        
        # Check for convergence
        diff_norm = linalg.norm(x - x_old, ord=float('inf'))
        if diff_norm < tol:
            break
            
    return x

solution = gauss_seidel(a, b, tol=1e-9, max_iter=100)

print("Gauss-Seidel solution for I1, I2, and I3:")
print(solution)
