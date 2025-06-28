import math

n = int(input())
k = len(str(n))
ans = 0
for i in range(k):
    ans += (n - math.pow(10, (k - i - 1)) + 1) * (k - i)
    n = math.pow(10, (k - i - 1)) - 1
print(int(ans))