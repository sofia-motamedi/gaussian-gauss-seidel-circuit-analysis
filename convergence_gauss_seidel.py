# diagram for gauss-seidel iterative method

import numpy as np
import matplotlib.pyplot as plt  # To plot the chart

# Define the coefficient matrix a and constant vector b.
a = np.array([[6, -4, 0],
              [-4, 9, -2],
              [0, -2, 7]], float)
b = np.array([10, 5, 8], float)

def gauss_seidel(a, b, tol=1e-9, max_iter=100):
    n = len(b)
    x = np.zeros(n, float)
    history = [x.copy()]  # To store values of x at each iteration

    for iteration in range(max_iter):
        x_old = x.copy()

        # Update each variable sequentially
        for i in range(n):
            sum_before = sum(a[i, j] * x[j] for j in range(i))
            sum_after = sum(a[i, j] * x_old[j] for j in range(i + 1, n))
            x[i] = (b[i] - sum_before - sum_after) / a[i, i]

        history.append(x.copy())

        # Check convergence
        if np.linalg.norm(x - x_old, np.inf) < tol:
            print(f"Converged after {iteration + 1} iterations.")
            break

    return x, history

solution, history = gauss_seidel(a, b)

# Log the history of values for I1, I2, and I3
iterations = range(len(history))
I1_values = [x[0] for x in history]
I2_values = [x[1] for x in history]
I3_values = [x[2] for x in history]

print("Gauss-Seidel solution for I1, I2, and I3:")
print(solution)

# Plot the chart of I1, I2, and I3 values over iterations
plt.figure(figsize=(10, 6))
plt.plot(iterations, I1_values, label='I1', marker='o')
plt.plot(iterations, I2_values, label='I2', marker='s')
plt.plot(iterations, I3_values, label='I3', marker='^')
plt.xlabel('Iteration Number')
plt.ylabel('Current Values (a)')
plt.title('Convergence of I1, I2, and I3 over Iterations')
plt.legend()
plt.grid()
plt.show()
