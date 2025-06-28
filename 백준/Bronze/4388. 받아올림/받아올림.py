while True:
    a, b = map(str, input().split())
    if a == '0' and b == '0':
        break
    k = 10 - len(a)
    a = '0' * k + a
    k = 10 - len(b)
    b = '0' * k + b
    tmp = 0
    cnt = 0

    for _ in range(10):
        if int(a[-1]) + int(b[-1]) + tmp > 9:
            cnt += 1
            tmp += 1
        else:
            tmp = 0
        
        a = a[:-1]
        b = b[:-1]

    print(cnt)