n = list(map(int, input().split()))
result = []
for i in n:
    if i not in result:
        result.append(i)
print("Without Duplicates : ", result)