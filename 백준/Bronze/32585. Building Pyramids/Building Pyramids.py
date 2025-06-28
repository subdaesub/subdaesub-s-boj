n = int(input())
cnt = 0
while n > 0:
    cnt += n * (n + 1) // 2
    n -= 1
print(cnt)