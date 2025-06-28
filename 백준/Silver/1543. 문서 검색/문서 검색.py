s = input()
k = input()

cnt = 0
i = 0
while len(k) + i <= len(s):
    if s[i:i + len(k)] == k:
        cnt += 1
        s = s[:i] + s[i + len(k):]
    else:
        i += 1

print(cnt)