p, q = map(int, input().split())
a, b = map(int, input().split())
if q > p:
    print(p * a + (q - p) * b)
else:
    print(q * a)