while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    min_gap = abs(a - 1)
    i = 2
    while True:
        if abs(a - i**b) < min_gap:
            min_gap = abs(a - i**b)
            i += 1
        else:
            i -= 1
            break
    print(i)