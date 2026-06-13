# Recursive Matrix Multiplication

def multiply_recursive(A, B, C, i, j, k, n):
    # If we reached end of row i
    if i >= n:
        return

    # If we reached end of column j
    if j >= n:
        multiply_recursive(A, B, C, i + 1, 0, 0, n)
        return

    # If k < n, continue multiplication
    if k < n:
        C[i][j] += A[i][k] * B[k][j]
        multiply_recursive(A, B, C, i, j, k + 1, n)
    else:
        # Move to next column
        multiply_recursive(A, B, C, i, j + 1, 0, n)

# Main program
n = 2  # size of matrix

A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

# Initialize result matrix with 0
C = [[0 for _ in range(n)] for _ in range(n)]

# Call recursive function
multiply_recursive(A, B, C, 0, 0, 0, n)

# Print result
print("Result Matrix:")
for row in C:
    print(row)


# Time Complexity = O(n^3) => same as iterative matrix multiplication. 