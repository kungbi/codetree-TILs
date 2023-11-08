N, M = tuple(map(int, input().split()))

items = [list(map(int, input().split())) for _ in range(N)]

items.sort(lambda item: item[1] / item[0], reverse=True)

price = 0
for item in items:
    if item[0] <= M:
        M -= item[0]
        price += item[1]
    elif item[0] > M:
        price += item[1] * (M / item[0])
        break
print(format(round(price, 3), ".3f"))