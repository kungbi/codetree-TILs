from heapq import *

n = int(input())
arr = list(map(int, input().split()))
heap = heapify(arr)

cost = 0
while n != 1:
    a = heappop(arr)
    b = heappop(arr)
    cost += a + b
    heappush(arr, a + b)
    n -= 1
print(cost)