# gaussian-gauss-seidel-circuit-analysis
Solving a 3-loop electric circuit using Gaussian elimination, improved Gaussian, and Gauss-Seidel methods.
# Numerical Methods for Electric Circuit Analysis

This project analyzes a three-loop electric circuit with independent voltage sources and shared resistors.  
The unknowns are the loop currents \( I_1, I_2, I_3 \), and the system of equations is derived using Kirchhoff's Voltage Law (KVL).

## Problem description

We consider a circuit with:
- Three loops, each with a voltage source \( E_1, E_2, E_3 \)
- Five resistors \( R_1, R_2, R_3, R_4, R_5 \)
- Shared resistors between loops (R3 between loops 1 and 2, R4 between loops 2 and 3)

Using KVL, the system of linear equations for \( I_1, I_2, I_3 \) is:

\[
\begin{aligned}
(R_1 + R_3) I_1 - R_3 I_2 &= E_1 \\
-R_3 I_1 + (R_2 + R_3 + R_4) I_2 - R_4 I_3 &= E_2 \\
-R_4 I_2 + (R_4 + R_5) I_3 &= E_3
\end{aligned}
\]

With the numerical values:
- \( R_1 = 2 \Omega, R_2 = 3 \Omega, R_3 = 4 \Omega, R_4 = 2 \Omega, R_5 = 5 \Omega \)
- \( E_1 = 10 \text{ V}, E_2 = 5 \text{ V}, E_3 = 8 \text{ V} \)

The analytical solution is approximately:
- \( I_1 \approx 3.28 \text{ A} \)
- \( I_2 \approx 2.42 \text{ A} \)
- \( I_3 \approx 1.83 \text{ A} \)

## Methods implemented

The system is solved using three numerical methods:

1. Gaussian Elimination (with partial pivoting)  
   - Implemented in src/gaussian_elimination.py
   - Produces the loop currents \( I_1, I_2, I_3 \)

2. Improved Gaussian Elimination with Iterative Refinement  
   - Implemented in src/gaussian_improved.py
   - Uses iterative refinement to reduce the residual and improve accuracy

3. Gauss–Seidel Iterative Method  
   - Implemented in src/gauss_seidel.py
   - Iteratively updates the currents and checks convergence
   - A convergence plot of \( I_1, I_2, I_3 \) over iterations is included in figures/convergence_gauss_seidel.png

All three methods converge to the same solution:
\[
I_1 \approx 3.28099,\quad I_2 \approx 2.42149,\quad I_3 \approx 1.83471
\]

## Files

- src/gaussian_elimination.py – Basic Gaussian elimination with partial pivoting
- src/gaussian_improved.py – Gaussian elimination + iterative refinement
- src/gauss_seidel.py – Gauss–Seidel iterative solver and convergence tracking
- report/Numerical_Methods_Electric_Circuit_Sofia_Motamedi.pdf – Full project report (in Persian) with derivations, code, and discussion
- figures/convergence_gauss_seidel.png – Convergence plot of the iterative method

## How to run

Requires Python and NumPy:

`bash
pip install numpy matplotlib
python src/gaussian_elimination.py
python src/gaussian_improved.py
python src/gauss_seidel.py
