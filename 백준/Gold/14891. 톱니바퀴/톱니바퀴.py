def clockwise(s):
    return s[-1] + s[:-1]

def counter(s):
    return s[1:] + s[0]

wheel = ['']
for _ in range(4):
    wheel.append(input())

k = int(input())
for _ in range(k):
    n, d = map(int, input().split())
    rotate = [0] * 5
    rotate[n] = d
    
    for i in range(n, 1, -1):
        if wheel[i][6] != wheel[i - 1][2]:
            rotate[i - 1] = -rotate[i]
        else:
            break

    for i in range(n, 4):
        if wheel[i][2] != wheel[i + 1][6]:
            rotate[i + 1] = -rotate[i]
        else:
            break

    for i in range(1, 5):
        if rotate[i] == 1:
            wheel[i] = clockwise(wheel[i])
        elif rotate[i] == -1:
            wheel[i] = counter(wheel[i])

cnt = 0
for i in range(1, 5):
    cnt += int(wheel[i][0]) * pow(2, i - 1)
print(cnt)