rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = []
for i in range(rows):
    row =[]
    for j in range(cols):
        num =int(input())
        row.append(num)
    matrix.append(row)
print(matrix)

largest = matrix[0][0]
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] > largest:
            largest = matrix[i][j]
print("Largest Element: ", largest)