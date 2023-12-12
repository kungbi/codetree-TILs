import sys
input = sys.stdin.readline

n = int(input())
a_arr = []
for _ in range(n):
    a_arr.append(int(input()))

b_arr = []
for num in range(1, n * 2 + 1):
    if num not in a_arr:
        b_arr.append(num)

score = 0
a_arr.sort()
b_arr.sort()
ai = bi = 0
while ai < n and bi < n:
    if a_arr[ai] < b_arr[bi]:
        ai += 1
        score += 1
    bi += 1

print(score)