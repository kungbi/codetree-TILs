n = int(input())
arr = list(map(int, input().split()))

max_num = -1001
result = 0
for num in arr:
    if (result < 0):
        max_num = max(max_num, result)
        result = num
    else:
        result += num
max_num = max(max_num, result)
print(max_num)