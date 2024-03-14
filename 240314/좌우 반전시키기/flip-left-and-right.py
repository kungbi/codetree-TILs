def push(arr, i):
    arr[i - 1] = (arr[i - 1] + 1) % 2
    arr[i] = (arr[i] + 1) % 2
    if i + 1 < len(arr):
        arr[i + 1] = (arr[i + 1] + 1) % 2


n = int(input())
arr = list(map(int, input().split()))

result = 0
for i in range(1, n):
    if arr[i - 1] == 0:
        push(arr, i)
        result += 1

print(result)