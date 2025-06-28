def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


a, b = map(int, input().split())
c, d = map(int, input().split())
a *= d
c *= b
b *= d
k = a + c
t = gcd(k, b)
print(k//t, b//t)