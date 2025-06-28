def not_sqrt(n, mobius):
    p = 0
    for i in range(1, int(n**0.5) + 1):
        p += mobius[i] * (n // (i**2))
    return p

def mobius(n):
    mobius = [0] * (n + 1)
    mobius[1] = 1
    for i in range(1, n + 1):
        if mobius[i]:
            for j in range(i * 2, n + 1, i):
                mobius[j] -= mobius[i]
    return mobius

def cal(l, r, k, mobius):
    while l < r - 1:
        mid = (l + r) // 2
        if not_sqrt(mid, mobius) < k:
            l = mid
        else:
            r = mid
    return r

k = int(input())
mobius = mobius(40558)
result = cal(0, 1644934081, k, mobius)
print(result)