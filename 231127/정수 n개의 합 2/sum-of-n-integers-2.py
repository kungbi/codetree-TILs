n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

prefix_sum = [0] * n
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]

k -= 1
max_num = 0
for i in range(n - k):
    num_i = prefix_sum[i + k] - prefix_sum[i] + arr[i]
    max_num = max(num_i, max_num)
print(max_num)