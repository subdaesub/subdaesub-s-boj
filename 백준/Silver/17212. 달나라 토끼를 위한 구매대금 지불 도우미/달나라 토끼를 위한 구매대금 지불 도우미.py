n = int(input())

if n == 3:
    print(2)
else:
    arr = [0, 1, 1, 1, 2, 1, 2]
    if n % 7 == 0:
        print(n // 7)
    elif n % 7 in (4, 6):
        print((n // 7) + 2)
    else:
        print((n // 7) + 1)