import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    res = 0
    while n > 0:
        res += n * n
        n -= 1
    print(res)