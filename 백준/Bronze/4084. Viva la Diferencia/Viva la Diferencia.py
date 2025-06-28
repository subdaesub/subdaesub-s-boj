while True:
    arr = list(map(int, input().split()))
    if sum(arr) == 0:
        break
    cnt = 0
    while True:
        if arr[0] == arr[1] and arr[1] == arr[2] and arr[2] == arr[3] and arr[3] == arr[0]:
            print(cnt)
            break
        a = abs(arr[0] - arr[1])
        b = abs(arr[1] - arr[2])
        c = abs(arr[2] - arr[3])
        d = abs(arr[3] - arr[0])
        arr[0] = a
        arr[1] = b
        arr[2] = c
        arr[3] = d
        cnt += 1