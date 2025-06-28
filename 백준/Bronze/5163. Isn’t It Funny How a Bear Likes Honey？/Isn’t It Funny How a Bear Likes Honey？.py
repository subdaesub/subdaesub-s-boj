import math
n = int(input())
for i in range(1, n + 1):
    k, w = map(float, input().split())
    cnt = 0
    for _ in range(int(k)):
        x = float(input())
        cnt += math.pi * (4 / 3) * x*x*x
    print(f'Data Set {i}:')
    if cnt > (w * 1000):
        print('Yes\n')
    else:
        print('No\n')