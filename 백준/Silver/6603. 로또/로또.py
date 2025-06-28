while True:
    k = list(map(int, input().split()))
    if k == [0]:
        break
    n = k[0]
    k = k[1:]
    for a in range(0, (n - 5)):
        for b in range(a + 1, (n - 4)):
            for c in range(b + 1, (n - 3)):
                for d in range(c + 1, (n - 2)):
                    for e in range(d + 1, (n - 1)):
                        for f in range(e + 1, n):
                            print(k[a], k[b], k[c], k[d], k[e], k[f])
    print('')