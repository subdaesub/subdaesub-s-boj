import sys
input = sys.stdin.readline

n = int(input())
l, m = 0, 0
for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        l += 1
    elif b > a:
        m += 1
print(l, m)