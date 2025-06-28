n = int(input())
cnt = 99
if n < 100:
    print(n)
else:
    for i in range(100, (n + 1)):
        a = int(str(i)[0])
        b = int(str(i)[1])
        c = int(str(i)[2])
        if b * 2 == a + c:
            cnt += 1
    print(cnt)