arr = [[1], [2, 4, 8, 6], [3, 9, 7, 1], [4, 6], [5], [6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1]]

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a % 10 == 0:
        print(10)
    else:
        a %= 10
        k = b % len(arr[a - 1])
        print(arr[a - 1][k - 1])