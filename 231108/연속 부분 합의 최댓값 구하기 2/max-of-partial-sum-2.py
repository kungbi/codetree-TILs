n = int(input())
arr = list(map(int, input().split()))

result = 0
for num in arr:
    if (result < 0):
        result = num
    else:
        result += num
print(result)