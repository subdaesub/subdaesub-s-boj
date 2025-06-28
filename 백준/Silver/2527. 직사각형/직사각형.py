for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    w = min(p1, p2) - max(x1, x2)
    h = min(q1, q2) - max(y1, y2)
    if w < 0 or h < 0:
        print('d')
    elif w == 0 and h == 0:
        print('c')
    elif w == 0 or h == 0:
        print('b')
    else:
        print('a')