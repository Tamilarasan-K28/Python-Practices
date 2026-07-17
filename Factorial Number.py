"""num = int(input("Enter a Number: "))
fact = 1
for i in range(1, num+1):
    fact *= i
print(f"Factorial of {num} is {fact}.")
"""
def factors(num):
    for i in range(1,num+1):
        if num % i == 0:
            print(i)

n = int(input("Enter a Number: "))
factors(n)