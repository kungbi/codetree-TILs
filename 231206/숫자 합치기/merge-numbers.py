n = int(input())
arr = list(map(int, input().split()))


cost = 0
while n != 1:
    arr.sort(reverse=True)
    a = arr.pop()
    b = arr.pop()
    cost += a + b
    arr.append(a + b)
    n -= 1
print(cost)