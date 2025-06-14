n = int(input())

cnt = 0

if n == 3:
    print(2)
else:
    cnt += n // 7

    x = n % 7

    if x in (4, 6):
        cnt += 2
    elif x == 0:
        pass
    else:
        cnt += 1

    print(cnt)