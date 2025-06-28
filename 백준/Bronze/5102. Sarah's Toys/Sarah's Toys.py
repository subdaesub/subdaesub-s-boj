while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    k = a - b
    if k < 2:
        print('0 0')
    else:
        if k % 2 == 0:
            print(k // 2, '0')
        else:
            print((k - 3) // 2, '1')