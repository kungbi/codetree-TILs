import sys
from heapq import heappop
from heapq import heappush


def input():
    return sys.stdin.readline().rstrip()


def solution():
    n = int(input())
    arr = []
    for _ in range(n):
        s, t = map(int, input().split())
        arr.append((s, t))

    arr.sort(key=lambda x: x[1])
    arr_i = n - 1
    heap = []
    score = 0
    for i in range(10000, 0, -1):
        while 0 <= arr_i and i <= arr[arr_i][1]:
            heappush(heap, -arr[arr_i][0])
            arr_i -= 1

        if heap:
            score += -heappop(heap)
    print(score)


solution()