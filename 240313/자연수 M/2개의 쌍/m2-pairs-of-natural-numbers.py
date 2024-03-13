import sys
from heapq import heappop
from heapq import heappush


def input():
    return sys.stdin.readline().rstrip()


def solution():
    n = int(input())
    heap = []
    for _ in range(n):
        x, y = map(int, input().split())
        for _ in range(x):
            heappush(heap, -y)
    
    result = float('inf')
    while 2 <= len(heap):
        a = -heappop(heap)
        b = -heappop(heap)
        c = a * b
        result = min(result, c)

    print(result)


solution()