arr = list(map(int,input().split()))
 
result = []
for i in arr:
    if i not in result:
        result.append(i)

print(result)