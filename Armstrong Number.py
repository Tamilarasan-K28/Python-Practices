"""n = int(input("Enter a Number:"))
sum_of_digits =0
digits = 0
temp = n
while temp > 0:
    digits +=1
    temp = temp // 10 
temp = n
while temp > 0:
    digit = temp% 10
    sum_of_digits += digit**digits
    temp //= 10
if sum_of_digits == n:
    print(n, "is an Armstrong Number.")
else:
    print(n, "is not an Armstrong Number.")
"""
n = int(input("Enter a Number:"))
sum_of_digits =0
digits = len(str(n))
temp = n
while temp > 0:
    digit = temp% 10
    sum_of_digits += digit**digits
    temp //= 10
if sum_of_digits == n:
    print(n, "is an Armstrong Number.")
else:
    print(n, "is not an Armstrong Number.")


