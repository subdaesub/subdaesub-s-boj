import math

n = int(input())
s = input()
k = s.count('C')
print(math.ceil(k / (n - k + 1)))