n = int(input())
count = 0

while n % 5 != 0:
    count += 1
    n -= 2
if n < 0:
    print(-1)
else:
    count += n // 5
    print(count)