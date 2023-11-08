n = int(input())
arr = list(map(int, input().split()))

result = arr[0]
for num in arr[1:]:
    if (0 < result):
        result += num
    else:
        result = num
print(result)