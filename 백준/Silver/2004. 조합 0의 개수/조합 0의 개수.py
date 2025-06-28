def fac(n, k):
    cnt = 0
    t = k
    while n >= t:
        cnt += n // t
        t *= k
    return cnt

n, m = map(int, input().split())
print(min(fac(n, 2) - fac(m, 2) - fac((n - m), 2), fac(n, 5) - fac(m, 5) - fac((n - m), 5)))