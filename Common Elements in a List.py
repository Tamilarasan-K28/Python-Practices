num1 = list(map(int,input("Enter List1 Values: ").split()))
num2 = list(map(int,input("Enter List2 Values: ").split()))
common = []
for i in num1:
    if i in num2 and i not in common:
        common.append(i)
print("Common Elements : ",common)