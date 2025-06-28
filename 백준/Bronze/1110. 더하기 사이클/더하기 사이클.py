n = int(input())
goal = n
cnt = 0
while True:
    if n < 10:
        k = n * 11
    else:
        k = int(str(n)[1]) * 10 + int((int(str(n)[0]) + int(str(n)[1])) % 10)
    cnt += 1
    if k == goal:
        break
    else:
        n = k
print(cnt)