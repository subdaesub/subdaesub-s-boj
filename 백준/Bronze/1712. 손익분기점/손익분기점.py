import math
a, b, c = map(int, input().split())
if b >= c:
    print(-1)
else:
    print(math.ceil(a / (c - b) + 0.00001))