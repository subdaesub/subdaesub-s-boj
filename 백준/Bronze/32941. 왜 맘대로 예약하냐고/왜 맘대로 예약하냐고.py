t, x = map(int, input().split())
n = int(input())
clk = True
for _ in range(n):
    k = int(input())
    arr = list(map(int, input().split()))
    if x in arr:
        pass
    else:
        clk = False
if clk:
    print('YES')
else:
    print('NO')