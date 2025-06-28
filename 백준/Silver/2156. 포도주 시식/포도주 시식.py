import sys
input = sys.stdin.readline

n = int(input())
arr = []
dp = []
for _ in range(n):
  arr.append(int(input()))

if n < 3:
  print(sum(arr))
else:
  dp.append(arr[0] + arr[1])
  dp.append(arr[0] + arr[2])
  dp.append(arr[1] + arr[2])
  if n == 3:
    print(max(dp))
  else:
    for i in range(3, n):
      a = dp[0]
      b = dp[1]
      c = dp[2]
      dp[0] = max(a, b, c)
      dp[1] = a + arr[i]
      dp[2] = b + arr[i]
    print(max(dp))