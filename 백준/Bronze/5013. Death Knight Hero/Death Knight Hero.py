n = int(input())
cnt = 0
for _ in range(n):
    s = input()
    if 'CD' not in s:
        cnt += 1
print(cnt)