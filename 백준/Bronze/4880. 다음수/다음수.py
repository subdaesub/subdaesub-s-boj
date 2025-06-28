while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if b * 2 == a + c:
        print(f"AP {c + (b - a)}")
    else:
        print(f"GP {c * (b // a)}")
