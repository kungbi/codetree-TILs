n = int(input())
arr = list(map(int, input().split()))
profit_arr = [0] * n
buy = arr[0]

for i in range(1, n):
    profit = arr[i] - buy
    if 0 < profit:
        profit_arr[i] = profit
    else:
        buy = arr[i]
    
print(max(profit_arr))