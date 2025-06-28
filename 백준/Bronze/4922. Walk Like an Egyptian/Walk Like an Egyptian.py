while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(f"{n} => {(n * (n - 1)) + 1}")