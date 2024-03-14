import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def solution():
    n = int(input())
    arr = []
    for _ in range(n):
        x, y = map(int, input().split())
        arr.append((x, y))

    arr.sort(key=lambda x: x[1])
    result = -1
    left_i = 0
    right_i = n - 1
    while left_i <= right_i:
        lx, ly = arr[left_i]
        rx, ry = arr[right_i]

        result = max(result, ly + ry)

        if lx > rx:
            arr[left_i] = (lx - rx, ly)
            right_i -= 1
        elif lx < rx:
            arr[right_i] = (rx - lx, ry)
            left_i += 1
        else:
            left_i += 1
            right_i -= 1
    print(result)


solution()