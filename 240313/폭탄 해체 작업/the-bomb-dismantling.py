import sys

def input():
    return sys.stdin.readline().rstrip()


n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
arr.sort(key= lambda x: x[1])
arr.reverse()

t = 0
score = 0
while arr:
    tmp = []
    tmp.append(arr.pop())
    while arr and arr[-1][1] == tmp[0][1]:
        tmp.append(arr.pop())
    max_score = 0
    for b in tmp:
        max_score = max(max_score, b[0])
    score += max_score
    t += 1
print(score)