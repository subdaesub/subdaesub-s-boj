from itertools import combinations

l, c = map(int, input().split())
arr = list(map(str, input().split()))
arr.sort()
vow = ['a', 'e', 'i', 'o', 'u']
for i in combinations(arr, l):
    clk_con = 0
    clk_vow = 0
    clk = False
    for j in i:
        if j in vow:
            clk_vow += 1
        else:
            clk_con += 1
        if clk_con >= 2 and clk_vow >= 1:
            clk = True
            break
    if clk:
        print("".join(i))