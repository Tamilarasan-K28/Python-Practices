"""
num = int(input("Enter a Number: "))
rev = 0
temp = num
while temp > 0:
    digit = temp % 10
    rev = rev*10 + digit
    temp //= 10
if rev == num:
    print(num, "is a Palindrome.")
else:
    print(num, "is not a Palindrome.")

"""

num = int(input("Enter a Number: "))
temp = str(num)
if num == int(temp[::-1]):
    print(num, "is a Palindrome.")
else:
    print(num, "is not a Palindrome.")
