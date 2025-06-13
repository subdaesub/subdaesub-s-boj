n = int(input())
m = int(input())
s = input()
cnt = 0
i = 0
ans = 0
while i < m - 2:
    if s[i] == 'I' and s[i+1] == 'O' and s[i+2] == 'I':
        cnt += 1
        i += 2
    else:
        if cnt >= n:
            ans += (cnt - n + 1)
        cnt = 0
        i += 1
if cnt >= n:
    ans += (cnt - n + 1)

print(ans)