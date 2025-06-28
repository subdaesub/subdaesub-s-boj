import sys
import bisect

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

l = []
k = []
p = [-1] * n

for i in range(n):
    pos = bisect.bisect_left(l, a[i])
    if pos == len(l):
        l.append(a[i])
        k.append(i)
    else:
        l[pos] = a[i]
        k[pos] = i

    if pos > 0:
        p[i] = k[pos - 1]

cnt = k[-1]

lst = []
while cnt != -1:
    lst.append(a[cnt])
    cnt = p[cnt]

print(len(l))
print(" ".join(map(str, lst[::-1])))