import sys
input = sys.stdin.readline

def ansubin(n, a):
    cnt = 0
    k = str(n * a)
    for i in k:
        if i in ['1', '3', '5', '7', '9']:
            cnt += 1
    if cnt % 2 != 0:
        print(k)
    else:
        ansubin(n, a * 2)

t = int(input())
for _ in range(t):
    n = int(input())
    ansubin(n, 1)