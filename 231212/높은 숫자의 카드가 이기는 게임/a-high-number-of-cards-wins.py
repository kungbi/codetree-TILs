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
for a in a_arr:
    for b in b_arr:
        if a < b:
            score += 1
            b_arr.remove(b)
            break
        b_arr.remove(b)
        
print(score)