import sys
input = sys.stdin.readline
from itertools import product

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

ans = list(product(arr, repeat = m))

for i in ans:
    print(*i)