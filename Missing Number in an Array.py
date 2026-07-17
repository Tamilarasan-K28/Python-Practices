arr = [1, 3, 4, 5]
n = 5
total = n * (n + 1) // 2
sum_arr = 0

for i in arr:
    sum_arr += i
miss = total - sum_arr

print("Missing Number =", miss)