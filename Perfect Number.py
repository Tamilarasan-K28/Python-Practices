n = int(input("Enter a Number: "))
sum_of_factors = 0
for i in range(1,n):
    if n % i ==0:
        sum_of_factors += i
if sum_of_factors == n:
    print(n,"is a Perfect Number.")
else:
    print(n,"is not a Perfect Number.")
