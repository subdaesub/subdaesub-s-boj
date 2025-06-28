n = int(input())
l = list(map(int, input().split()))
for i in range(500000, -1, -1):
    k = l[0] % i
    clk = True
    for j in l:
        if j % i != k:
            clk = False
            break
    if clk:
        print(i)
        break
    else:
        clk = True