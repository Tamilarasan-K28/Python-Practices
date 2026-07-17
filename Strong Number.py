n = int(input("Enter a Number: "))
temp = n
sum_of_fact = 0
while temp > 0:
    digit = temp % 10
    fact = 1
    for i in range(1, digit+1):
        fact *= i
    sum_of_fact += fact
    temp //= 10
if sum_of_fact == n:
    print(n,"is a Strong Number")
else:
    print(n,"is not a Strong Number")