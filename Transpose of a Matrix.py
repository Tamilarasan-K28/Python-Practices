matrix = [[1, 2, 3], [4, 5, 6]]
rows = len(matrix)
cols = len(matrix[0])

for i in range(cols):
    for j in range(rows):
        print(matrix[j][i], end=" ")
    print()