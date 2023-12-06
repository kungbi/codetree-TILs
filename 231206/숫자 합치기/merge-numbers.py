n = int(input())
arr = list(map(int, input().split()))

def f(input_list, cost):
    input_list.sort()
    n = len(input_list)
    tmp_list = []

    for i in range(0, n - 1, 2):
        tmp_list.append(input_list[i] + input_list[i+1])
        cost += input_list[i] + input_list[i+1]
    if n % 2 == 1:
        tmp_list.append(input_list[n - 1])
    if len(tmp_list) != 1:
        return f(tmp_list, cost)
    return cost

result = f(arr, 0)
print(result)