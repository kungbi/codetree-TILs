n = int(input())
before = input()
after = input()

result = 0
flag = 0
for i in range(n):
    if before[i] != after[i]:
        flag = 1
    elif before[i] == after[i] and flag == 1:
        flag = 0
        result += 1
if flag == 1:
    result += 1
print(result)