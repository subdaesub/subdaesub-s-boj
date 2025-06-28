x = input()
y = input()
a = abs(ord(y[0]) - ord(x[0]))
b = abs(int(y[1]) - int(x[1]))
if a <= b:
    print(a, b)
else:
    print(b, a)