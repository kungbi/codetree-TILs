import sys
input = sys.stdin.readline

n = int(input())
b_arr = []
for _ in range(n):
    b_arr.append(int(input()))
b_set = set(b_arr)

a_arr = [
    num for num in range(1, 2 * n + 1) if num not in b_set
]

a_arr.sort()
b_arr.sort()
score = 0
a_idx = b_idx = 0
while a_idx < n and b_idx < n:
    if a_arr[a_idx] > b_arr[b_idx]:
        b_idx += 1
        score += 1
    a_idx += 1

print(score)