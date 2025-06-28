a, b = map(int, input().split())
c, d = map(int, input().split())
s = a + b + c + d - 1
if s % 4 == 0:
    print(4)
else:
    print(s % 4)