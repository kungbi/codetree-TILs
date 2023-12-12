n = int(input())
a_arr = []
for _ in range(n):
    a_arr.append(int(input()))

b_arr = []
for num in range(1, n * 2 + 1):
    if num not in a_arr:
        b_arr.append(num)

score = 0
b_arr.sort()
for i in range(n):
    for num in b_arr:
        if a_arr[i] < num:
            score += 1
            b_arr.remove(num)
print(score)