N, M = tuple(map(int, input().split()))

items = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    price_per = items[i][1] / items[i][0]
    items[i].append(price_per)
items.sort(lambda item: item[2], reverse=True)

price = 0
for item in items:
    if item[0] <= M:
        M -= item[0]
        price += item[1]
    elif item[0] > M:
        price += item[1] * (M / item[0])
        break
print(format(round(price, 3), ".3f"))