import math
def Is_prime(n):
    clk = True

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            clk = False
            break
    return clk

while True:
    n = int(input())
    cnt = 0
    if n == 0:
        break
    if n == 1:
        cnt = 1
    for i in range(n + 1, 2 * n + 1):
        if i % 2 != 0:
            if Is_prime(i):
                cnt += 1
    print(cnt)