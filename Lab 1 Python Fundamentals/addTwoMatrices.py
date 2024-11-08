# Python Program to Add Two Matrices

# Function to add two matrices
def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

# Input: dimensions of the matrices
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

# Input: first matrix
print("Enter elements of the first matrix:")
matrix1 = []
for i in range(rows):
    row = list(map(int, input(f"Enter row {i + 1}: ").split()))
    matrix1.append(row)

# Input: second matrix
print("Enter elements of the second matrix:")
matrix2 = []
for i in range(rows):
    row = list(map(int, input(f"Enter row {i + 1}: ").split()))
    matrix2.append(row)

result_matrix = add_matrices(matrix1, matrix2)

print("The sum of the two matrices is:")
for row in result_matrix:
    print(' '.join(map(str, row)))
