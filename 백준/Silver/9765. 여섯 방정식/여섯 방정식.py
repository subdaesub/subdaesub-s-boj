def GCD(x, y):
    while y:
        x, y = y, x % y
    return x

a, b, c, d, e, f = map(int, input().split())
x = GCD(a, e)
y = GCD(f, c)
print(a // x, x, e // x, f // y, y, c // y)