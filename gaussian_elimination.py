# gaussian elimination method

from numpy import array, zeros

# Define the variable (coefficient) matrix and the constant matrix
variable_matrix = array([[6, -4, 0],
                         [-4, 9, -2],
                         [0, -2, 7]], float)
constant_matrix = array([[10],
                         [5],
                         [8]], float)
n = len(constant_matrix)
x = zeros(n, float)

# Elimination with partial pivoting
for k in range(n - 1):
    # Pivoting step
    max_index = k
    for i in range(k + 1, n):
        if abs(variable_matrix[i, k]) > abs(variable_matrix[max_index, k]):
            max_index = i
    if max_index != k:
        variable_matrix[[k, max_index]] = variable_matrix[[max_index, k]]
        constant_matrix[[k, max_index]] = constant_matrix[[max_index, k]]

    # forward elimination for rows below the pivot row
    for i in range(k + 1, n):
        if variable_matrix[i, k] == 0:
            continue
        factor = variable_matrix[i, k] / variable_matrix[k, k]
        for j in range(k, n):
            variable_matrix[i, j] -= factor * variable_matrix[k, j]
        constant_matrix[i] -= factor * constant_matrix[k]

# Back substitution
x[n - 1] = constant_matrix[n - 1].item() / variable_matrix[n - 1, n - 1].item()
for i in range(n - 2, -1, -1):
    sum_ax = 0
    for j in range(i + 1, n):
        sum_ax += variable_matrix[i, j] * x[j]
    x[i] = (constant_matrix[i].item() - sum_ax) / variable_matrix[i, i].item()

print("The solutions for I1, I2 and I3 are:")
print(x)
