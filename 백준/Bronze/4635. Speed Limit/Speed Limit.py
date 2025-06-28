while True:
    n = int(input())
    if n == -1:
        break
    s = [0]
    t = [0]
    for _ in range(n):
        a, b = map(int, input().split())
        s.append(a)
        t.append(b)
    res = 0
    for i in range(n):
        res += (t[i + 1] - t[i]) * s[i + 1]
    print(f"{res} miles")