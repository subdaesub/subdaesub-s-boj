a, b = map(int, input().split())
for i in range(int(input())):
    n = int(input())
    if n > 1000:
        print(n, 1000 * a + (n - 1000) * b)
    else:
        print(n, n * a)