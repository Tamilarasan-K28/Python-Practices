num = list(map(int,input("Enter List Values: ").split()))
even = [i for i in num if i%2 == 0]
odd = [j for j in num if j%2 !=0]
print("Even : ",even)
print("Odd : ", odd)

