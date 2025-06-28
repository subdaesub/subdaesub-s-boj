while True:
    a, b = map(str, input().split())
    h = int(a[0:2]) + int(b[0:2])
    m = int(a[3:5]) + int(b[3:5])
    d = 0
    if h == 0 and m == 0:
        break
    
    if m > 59:
        h += 1
        m -= 60
    
    if h > 23:
        d += h // 24
        h %= 24
    
    if h < 10:
        h = '0' + str(h)
    
    if m < 10:
        m = '0' + str(m)

    if d == 0:
        print(str(h) + ':' + str(m))
    else:
        print(str(h) + ':' + str(m), f'+{d}')