n = int(input())
arr = list(map(int, input().split()))

max_num = -1001
result = -1001
for num in arr:
    if (0 < result):
        result += num
    else:
        max_num = max(max_num, result)
        result = num
print(max_num)