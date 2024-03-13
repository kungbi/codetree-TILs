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
        while heap and a_x % 2 == 1:
            a_y, a_x= heappop(heap)
        a_y *= -1

        if not heap:
            print(a_y)
            return

        b_y, b_x= heappop(heap)
        while heap and b_x % 2 == 1:
            b_y, b_x= heappop(heap)
        b_y *= -1

        result = min(result, a_y * b_y)

        
    print(result)


solution()