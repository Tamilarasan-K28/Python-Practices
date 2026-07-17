num = int(input("Enter a Number:"))
count = 0
if num <= 1:
    print(num, "is Not a Prime Number")
else:
    for i in range(2,num+1):
        if num % i == 0:
            count += 1
    if count == 1:
        print(num, "is a Prime Number")
    else:
        print(num, "is Not a Prime Number")
