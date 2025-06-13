n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = []
for _ in range(n):
    room.append(list(map(int, input().split())))
cnt = 0
clk = True
while True:
    if room[r][c] == 0:
        cnt += 1
        room[r][c] = 2
    else:
        if room[r + 1][c] == 0 or room[r - 1][c] == 0 or room[r][c + 1] == 0 or room[r][c - 1] == 0:
            if d == 0:
                d = 3
            else:
                d -= 1
            if d == 0:
                if room[r - 1][c] == 0:
                    r -= 1
            elif d == 1:
                if room[r][c + 1] == 0:
                    c += 1
            elif d == 2:
                if room[r + 1][c] == 0:
                    r += 1
            elif d == 3:
                if room[r][c - 1] == 0:
                    c -= 1
        else:
            if d == 0:
                if room[r + 1][c] == 1:
                    break
                else:
                    r += 1
            elif d == 1:
                if room[r][c - 1] == 1:
                    break
                else:
                    c -= 1
            elif d == 2:
                if room[r - 1][c] == 1:
                    break
                else:
                    r -= 1
            elif d == 3:
                if room[r][c + 1] == 1:
                    break
                else:
                    c += 1
print(cnt)