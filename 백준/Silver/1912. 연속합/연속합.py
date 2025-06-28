n = int(input())
arr = list(map(int, input().split()))

max_sum = arr[0]
dp = arr[0]

for i in range(1, n):
  dp = max(arr[i], dp + arr[i])
  max_sum = max(max_sum, dp)
  
print(max_sum)