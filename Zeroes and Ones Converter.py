"""
num = int(input("Enter a number: "))
temp = num
result = 0
place = 1
while temp > 0:
    digit = temp % 10
    if digit == 0:
        digit = 1
    elif digit == 1:
        digit = 0
    result = result + digit * place
    place =place * 10
    temp //= 10
print("Converted Number: ", result)

"""
num = int(input("Enter a number: "))
temp = str(num)
for i in temp:
    if temp[i] == '0':
        temp.replace('0','1')
    elif  temp[i] == '1':
        temp.replace('1','0')
print(temp)