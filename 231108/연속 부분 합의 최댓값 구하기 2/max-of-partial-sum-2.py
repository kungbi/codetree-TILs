n = int(input())
arr = list(map(int, input().split()))

max_num = -1001
sum_num = 0
for num in arr:
    if (sum_num < 0):
        sum_num = num
    else:
        sum_num += num
    max_num = max(max_num, sum_num)
print(max_num)