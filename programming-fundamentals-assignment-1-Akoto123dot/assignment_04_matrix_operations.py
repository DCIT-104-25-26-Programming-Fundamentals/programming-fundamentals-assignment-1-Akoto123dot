# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(rows, cols):
    matrix = []
    for r in range(rows):
        row = list(map(int, input(f"Enter row {r+1}: ").split()))
        matrix.append(row)
    return matrix

def display_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{val:4}" for val in row))
    print()

# -------------------------------
# PART A – Transpose a Matrix
# -------------------------------
def transpose(matrix):
    rows, cols = len(matrix), len(matrix[0])
    result = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        result.append(new_row)
    return result

# -------------------------------
# PART B – Add Two Matrices
# -------------------------------
def add_matrices(A, B):
    rows, cols = len(A), len(A[0])
    result = []
    for r in range(rows):
        new_row = []
        for c in range(cols):
            new_row.append(A[r][c] + B[r][c])
        result.append(new_row)
    return result

# -------------------------------
# PART C – Multiply Two Matrices
# -------------------------------
def multiply_matrices(A, B):
    rowsA, colsA = len(A), len(A[0])
    rowsB, colsB = len(B), len(B[0])
    result = [[0] * colsB for _ in range(rowsA)]
    for i in range(rowsA):
        for j in range(colsB):
            for k in range(colsA):
                result[i][j] += A[i][k] * B[k][j]
    return result

# ================================================================
# MAIN PROGRAM
# ================================================================
print("=== PART A: Transpose ===")
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = read_matrix(rows, cols)

print("Original Matrix:")
display_matrix(matrix)

transposed = transpose(matrix)
print("Transposed Matrix:")
display_matrix(transposed)

print("=== PART B: Addition ===")
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
A = read_matrix(rows, cols)
B = read_matrix(rows, cols)

print("Matrix A:")
display_matrix(A)
print("Matrix B:")
display_matrix(B)

sum_matrix = add_matrices(A, B)
print("Sum of Matrices:")
display_matrix(sum_matrix)

print("=== PART C: Multiplication ===")
rowsA = int(input("Enter rows for Matrix A: "))
colsA = int(input("Enter columns for Matrix A: "))
A = read_matrix(rowsA, colsA)

rowsB = int(input("Enter rows for Matrix B: "))
colsB = int(input("Enter columns for Matrix B: "))
B = read_matrix(rowsB, colsB)

print("Matrix A:")
display_matrix(A)
print("Matrix B:")
display_matrix(B)

if colsA != rowsB:
    print("Error: Cannot multiply, incompatible dimensions.")
else:
    product = multiply_matrices(A, B)
    print("Product of Matrices:")
    display_matrix(product)
