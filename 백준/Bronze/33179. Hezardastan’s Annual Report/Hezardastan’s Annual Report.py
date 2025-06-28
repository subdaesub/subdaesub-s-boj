n = int(input())
a = list(map(int, input().split()))
cnt = 0
for i in a:
    if i % 2 == 0:
        cnt += (i // 2)
    else:
        cnt += (i // 2) + 1
print(cnt)