n = int(input())


result = float('inf')
for i in range(20001):
    remain = n - 5 * i
    if 0 <= remain and remain % 2 == 0:
        result = min(result, i + remain // 2)
if result != float('inf'):
    print(result)
else:
    print(-1)