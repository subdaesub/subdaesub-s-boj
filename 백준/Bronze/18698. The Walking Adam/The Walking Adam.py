t = int(input())
cnt = 0
for _ in range(t):
    s = input()
    for char in s:
        if char != 'D':
            cnt +=1
        else:
            break
    print(cnt)
    cnt = 0