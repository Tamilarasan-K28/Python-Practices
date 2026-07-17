num1 = list(map(int,input("Enter List1 Values: ").split()))
num2 = list(map(int,input("Enter List2 Values: ").split()))
num3 = list(map(int,input("Enter List3 Values: ").split()))

inter = []
for i in num1:
    if i in num2 and i in num3 and i not in inter:
        inter.append(i)
print("Intersection: ",inter)