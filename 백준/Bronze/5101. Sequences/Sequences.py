while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if c == a:
        print(1)
    else:
        if (c - a) % b == 0 and (c - a) // b >= 0:
            print((c - a) // b + 1)
        else:
            print('X')