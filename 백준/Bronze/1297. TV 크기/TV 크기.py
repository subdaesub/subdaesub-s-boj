import math
a, b, c = map(int, input().split())
k = math.sqrt(a*a/(b*b + c*c))
print(int(b*k), int(c*k))