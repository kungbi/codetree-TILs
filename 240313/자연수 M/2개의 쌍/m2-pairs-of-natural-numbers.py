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
        heappush(heap, (-y, x))
    
    result = float('inf')
    while 2 <= len(heap):
        a_y, a_x= heappop(heap)
        if 1 < a_x:
            heappush(heap, (a_y, a_x - 1))
        
        b_y, b_x= heappop(heap)
        if 1 < b_x:
            heappush(heap, (b_y, b_x - 1))

        result = min(result, a_y * b_y)

        
    print(result)


solution()