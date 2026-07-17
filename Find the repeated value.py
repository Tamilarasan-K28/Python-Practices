num = list(map(int,input("Enter List Values: ").split()))
seen =[]
for i in num:
    if i in seen:
        print("First Repeated Element: ",i)
        break
    seen.append(i)