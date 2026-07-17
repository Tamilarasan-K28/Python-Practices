num = list(map(int,input().split()))
largest = 0
second = 0
for i in num:
    if i > largest:
        second = largest
        largest= i
    elif i > second and i != second:
        second = i
print("Second Largest Number: ",second)