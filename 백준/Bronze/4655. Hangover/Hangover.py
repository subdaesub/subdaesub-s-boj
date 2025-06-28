while True:
    n = float(input())
    if n == 0:
        break
    i = 2
    sum = 0
    while True:
        sum += (1 / i)
        if sum >= n:
            print(f"{i - 1} card(s)")
            break
        else:
            i += 1