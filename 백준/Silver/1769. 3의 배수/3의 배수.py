s = input()
cnt = 0
while len(s) > 1:
    tmp = 0
    for i in range(len(s)):
        tmp += int(s[i])
    s = str(tmp)
    cnt += 1

print(cnt)
if int(s) in [3, 6, 9]:
    print('YES')
else:
    print('NO')