n = int(input())


result = n // 5
n = n % 5

result += n // 2
n = n % 2

if n == 0:
    print(result)
else:
    print(-1)