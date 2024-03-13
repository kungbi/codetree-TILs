n = int(input())

result = 0
while n != 0:
    if 6 == n:
        n -= 6
        result += 3
        break
    elif 5 <= n:
        n -= 5
    elif 2 <= n:
        n -= 2
    else:
        result = -1
        break
    result += 1
print(result)