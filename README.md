# Numerical Solution of a Three-Loop Electrical Circuit

## Overview

This project investigates the numerical solution of a three-loop electrical circuit using systems of linear equations. The circuit is formulated using Kirchhoff's Voltage Law (KVL), and the resulting system is solved using several numerical methods.

The main objective is to compare direct and iterative numerical approaches for determining the unknown loop currents and to investigate the convergence behavior of the Gauss-Seidel iterative method.

---

## Problem Description

The circuit consists of three electrical loops, each containing an independent voltage source and several resistors.
<p align="center">
  <img src="figures/circuit.png">
</p>

The unknown loop currents are denoted by:

- \(I_1\): Current in Loop 1
- \(I_2\): Current in Loop 2
- \(I_3\): Current in Loop 3

Some resistors are shared between adjacent loops. Therefore, the current through a shared resistor is determined by the difference between the corresponding loop currents.

The circuit parameters used in this project are:

| Parameter | Value |
|---|---:|
| \(R_1\) | \(2\,\Omega\) |
| \(R_2\) | \(3\,\Omega\) |
| \(R_3\) | \(4\,\Omega\) |
| \(R_4\) | \(2\,\Omega\) |
| \(R_5\) | \(5\,\Omega\) |
| \(E_1\) | \(10\,V\) |
| \(E_2\) | \(5\,V\) |
| \(E_3\) | \(8\,V\) |

---

## Mathematical Formulation

Applying Kirchhoff's Voltage Law to the three loops gives the following system of linear equations:

<p align="center">
  <b>(R₁ + R₃)I₁ − R₃I₂ = E₁</b>
</p>

\[
-R_3I_1+(R_2+R_3+R_4)I_2-R_4I_3=E_2
\]

\[
-R_4I_2+(R_4+R_5)I_3=E_3
\]

Substituting the given circuit parameters results in:

\[
4I_1-4I_2=10
\]

\[
-4I_1+9I_2-2I_3=5
\]

\[
-2I_2+7I_3=8
\]

In matrix form:

\[
\begin{bmatrix}
4 & -4 & 0\\
-4 & 9 & -2\\
0 & -2 & 7
\end{bmatrix}
\begin{bmatrix}
I_1\\
I_2\\
I_3
\end{bmatrix}
=
\begin{bmatrix}
10\\
5\\
8
\end{bmatrix}
\]

---

## Numerical Methods

Three different approaches are considered in this project.

### 1. Analytical Solution

The system is first manipulated algebraically to obtain the unknown currents.

The reported values are approximately:

\[
I_1 \approx 3.28
\]

\[
I_2 \approx 2.42
\]

\[
I_3 \approx 1.83
\]

---

### 2. Gaussian Elimination

Gaussian elimination is used as a direct method for solving the system of linear equations.

The method transforms the coefficient matrix into an upper triangular form and then obtains the unknown currents using back substitution.

---

### 3. Improved Gaussian Elimination

An improved version of Gaussian elimination is also considered to provide a more robust direct solution procedure.

This approach is particularly useful when numerical stability and the effects of pivot selection need to be considered.

---

### 4. Gauss-Seidel Iterative Method

The Gauss-Seidel method is used as an iterative approach for solving the system.

Starting from an initial approximation, the unknown currents are updated iteratively until the solution converges.

The convergence of the three current values is investigated over successive iterations.

---

## Convergence Analysis

The following figure shows the convergence behavior of \(I_1\), \(I_2\), and \(I_3\) during the Gauss-Seidel iterations.

<p align="center">
  <img src="figures/convergence_gauss_seidel.png" alt="Convergence of I1, I2, and I3 over iterations" width="750">
</p>

As shown in the plot, the current values approach stable values after a relatively small number of iterations. After the initial iterations, the changes become very small, indicating convergence of the iterative procedure.

---

## Results

The project compares direct and iterative approaches for solving the same system of equations.

| Method | Type | Main Characteristic |
|---|---|---|
| Analytical Solution | Direct | Algebraic solution |
| Gaussian Elimination | Direct | Straightforward matrix-based solution |
| Improved Gaussian Elimination | Direct | Improved numerical treatment |
| Gauss-Seidel | Iterative | Requires convergence |
For a small three-variable system such as this one, Gaussian elimination and improved Gaussian elimination provide straightforward solutions. For larger systems or systems with a suitable structure, iterative methods such as Gauss-Seidel can become more useful.

---

## Implementation

The numerical calculations and iterative solution were implemented computationally. The project includes the calculation of the unknown currents and visualization of the convergence behavior of the Gauss-Seidel method.

### Main tasks

- Formulation of the circuit equations using KVL
- Construction of the corresponding linear system
- Analytical solution of the system
- Solution using Gaussian elimination
- Solution using improved Gaussian elimination
- Iterative solution using Gauss-Seidel
- Analysis and visualization of convergence
