# Python Program to Multiply Two Matrices

# Function to multiply two matrices
def multiply_matrices(matrix1, matrix2):
    # Get the number of rows and columns
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    
    # Check if multiplication is possible
    if cols1 != rows2:
        print("Matrix multiplication is not possible due to incompatible dimensions.")
        return None
    
    # Performing matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

# Input: dimensions of the matrices
rows1 = int(input("Enter the number of rows for the first matrix: "))
cols1 = int(input("Enter the number of columns for the first matrix: "))
rows2 = int(input("Enter the number of rows for the second matrix: "))
cols2 = int(input("Enter the number of columns for the second matrix: "))

# Input: first matrix
print("Enter elements of the first matrix:")
matrix1 = []
for i in range(rows1):
    row = list(map(int, input(f"Enter row {i + 1}: ").split()))
    matrix1.append(row)

# Input: second matrix
print("Enter elements of the second matrix:")
matrix2 = []
for i in range(rows2):
    row = list(map(int, input(f"Enter row {i + 1}: ").split()))
    matrix2.append(row)

# Multiplying the matrices
result_matrix = multiply_matrices(matrix1, matrix2)

if result_matrix is not None:
    print("The product of the two matrices is:")
    for row in result_matrix:
        print(' '.join(map(str, row)))
