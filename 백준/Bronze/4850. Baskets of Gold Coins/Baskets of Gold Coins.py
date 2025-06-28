while True:
    try:
        n, w, d, s = map(int, input().split())
        cnt = (n - 1) * n // 2 * w
        cnt -= s
        if cnt == 0:
            print(n)
        else:
            print(cnt // d)
    except EOFError:
        break