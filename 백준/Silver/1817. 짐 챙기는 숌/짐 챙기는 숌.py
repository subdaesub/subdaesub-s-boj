n, m = map(int, input().split())
if n == 0:
    print(0)
else:
    arr = list(map(int, input().split()))
    w = 0
    box = 1
    for i in range(n):
        if arr[i] + w > m:
            box += 1
            w = arr[i]
        else:
            w += arr[i]
    print(box)