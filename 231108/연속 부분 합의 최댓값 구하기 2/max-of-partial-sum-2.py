n = int(input())
arr = list(map(int, input().split()))

result = 0
for num in arr:
    if (result + num > 0):
        result += num
    else:
        result = num
print(result)