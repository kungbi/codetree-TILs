n, k = tuple(map(int, input().split()))

coins = []
for _ in range(n):
    coins.append(int(input()))
coins.reverse()

count = 0
while (0 < k):
    for coin in coins:
        if coin <= k:
            k -= coin
            count += 1
            break
print(count)