num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
a = num1
b = num2
while b > 0 :
    a,b = b, a %b
gcd = a
print(f"HCF of {num1} and {num2} is {gcd}")


"""
num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
hcf = 1
for i in range(1, min(num1,num2)+1):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
print(f"HCF of {num1} and {num2} is {hcf}")
"""