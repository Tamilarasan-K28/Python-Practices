num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
a = num1
b = num2
while b > 0 :
    a,b = b, a %b
gcd = a
lcm = (num1*num2)//gcd
print(f"LCM of {num1} and {num2} is {lcm}")