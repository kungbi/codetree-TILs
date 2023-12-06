n = int(input())
arr = []
for _ in range(n):
    arr.append(tuple(map(int, input().split())))

arr.sort(key=lambda x: x[1])
count = 0
t = 0
for i in range(n):
    if t <= arr[i][0]:
        count += 1
        t = arr[i][1]
print(count)