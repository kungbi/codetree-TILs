def push(arr, i):
    for i in range(i + 1):
        if arr[i] == 'G':
            arr[i] = 'H'
        else:
            arr[i] = 'G'

n = int(input())
before = list(input())
after = list(input())

result = 0
for i in range(n - 1, -1, -1):
    if before[i] != after[i]:
        push(before, i)
        result += 1

flag = 1
for i in range(n):
    if before[i] != after[i]:
        flag = 0
if flag:
    print(result)
else:
    print(-1)