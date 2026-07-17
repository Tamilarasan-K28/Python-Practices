arr = [1, 2, 2, 3, 1, 4, 2]

visited = []

for i in arr:
    if i not in visited:
        count = 0
        for j in arr:
            if i == j:
                count += 1
        print(i, "occurs", count, "times")
        visited.append(i)