def Is_prime(n):
    clk = True
    for i in range(2, n // 2):
        if n % i == 0:
            clk = False
            break
    return clk

t = int(input())
for _ in range(t):
    n = int(input())
    if n == 4:
        print(2, 2)
    else:
        a, b = n // 2, n // 2
        for i in range((n - 4) // 2):
            x = a - i
            y = b + i
            if x % 2 != 0:
                if Is_prime(x) and Is_prime(y):
                    print(x, y)
                    break