n = int(input())
arr = list(map(int, input().split()))

result = 0
for num in arr:
    if (0 < result):
        result += num
    else:
        result = num
print(result)