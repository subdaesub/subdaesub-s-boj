import math

def change(k):
    if k in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return int(ord(k)) - 48
    else:
        return ord(k) - 55
a, b = map(str, input().split())
b = int(b)
ans = 0
for i in range(len(a)):
    ans += change(a[i]) * int(math.pow(b, len(a) - i - 1))
print(ans)