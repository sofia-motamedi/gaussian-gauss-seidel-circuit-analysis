from numpy import array, zeros, dot, linalg

# Define the variable (coefficient) matrix and the constant matrix
variable_matrix = array([[6, -4, 0],
                         [-4, 9, -2],
                         [0, -2, 7]], float)
constant_matrix = array([10, 5, 8], float)
n = len(constant_matrix)
x = zeros(n, float)

# Gaussian elimination with partial pivoting
def gaussian_elimination(variable_matrix, constant_matrix):
    a = variable_matrix.copy()
    b = constant_matrix.copy()
    n = len(b)
    x = zeros(n, float)

    # Elimination with partial pivoting
    for k in range(n - 1):
        # Pivoting step
        max_index = k
        for i in range(k + 1, n):
            if abs(a[i, k]) > abs(a[max_index, k]):
                max_index = i
        if max_index != k:
            a[[k, max_index]] = a[[max_index, k]]
            b[[k, max_index]] = b[[max_index, k]]

        # Forward elimination for rows below the pivot row
        for i in range(k + 1, n):
            if a[k, k] == 0:
                raise ValueError("Zero pivot encountered!")
            factor = a[i, k] / a[k, k]
            for j in range(k, n):
                a[i, j] -= factor * a[k, j]
            b[i] -= factor * b[k]

    # Back substitution
    x[n - 1] = b[n - 1] / a[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        sum_ax = 0
        for j in range(i + 1, n):
            sum_ax += a[i, j] * x[j]
        x[i] = (b[i] - sum_ax) / a[i, i]

    return x

# Iterative Refinement
def iterative_refinement(variable_matrix, constant_matrix, tol=1e-9, max_iter=10):
    # Initial solution using Gaussian elimination
    x = gaussian_elimination(variable_matrix, constant_matrix)
    
    for iteration in range(max_iter):
        alpha = constant_matrix - dot(variable_matrix, x)
        alpha_norm = linalg.norm(alpha, ord=float('inf'))
        
        # Check if residual is below tolerance
        if alpha_norm < tol:
            break
            
        # Solve for correction using Gaussian elimination
        correction = gaussian_elimination(variable_matrix, alpha)
        x += correction
        
    return x

refined_solution = iterative_refinement(variable_matrix, constant_matrix)

print("Refined solutions for I1, I2, and I3:")
print(refined_solution)
