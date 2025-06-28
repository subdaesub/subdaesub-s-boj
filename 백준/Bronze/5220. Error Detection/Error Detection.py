t = int(input())
for _ in range(t):
    n, clk = map(int, input().split())
    k = str(bin(n))
    if k.count('1') % 2 == clk:
        print('Valid')
    else:
        print('Corrupt')