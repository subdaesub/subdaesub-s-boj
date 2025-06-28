n, k = map(int, input().split())
arr = [i for i in range(2, n + 1)]
clk = [False for _ in range(2, n + 1)]
cnt = 0
while True:
    for i in range(len(arr)):
        if not clk[i]:
            t = arr[i]
            break
    ans = 0
    for i in range(len(arr)):
        if arr[i] % t == 0 and not clk[i]:
            clk[i] = True
            cnt += 1
        if cnt == k:
            ans = arr[i]
            break
    if ans:
        print(ans)
        break