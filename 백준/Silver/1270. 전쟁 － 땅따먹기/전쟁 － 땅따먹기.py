n = int(input())

for _ in range(n):
    t = list(map(int, input().split()))
    t = t[1::]
    t.sort()
    k = t[len(t) // 2]
    if t.count(k) > (len(t) // 2):
        print(k)
    else:
        print('SYJKGW')