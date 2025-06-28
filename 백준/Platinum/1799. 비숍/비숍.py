N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

max_cnt = [0, 0]
used_1 = [False] * (2 * N)
used_2 = [False] * (2 * N)

def backtrack(pos, count, color):
    if pos >= len(black_white[color]):
        max_cnt[color] = max(max_cnt[color], count)
        return
    
    x, y = black_white[color][pos]
    d1 = x + y
    d2 = x - y + N - 1

    if not used_1[d1] and not used_2[d2]:
        used_1[d1] = used_2[d2] = True
        backtrack(pos + 1, count + 1, color)
        used_1[d1] = used_2[d2] = False

    backtrack(pos + 1, count, color)


black_white = [[], []]
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            color = (i + j) % 2
            black_white[color].append((i, j))

backtrack(0, 0, 0)
backtrack(0, 0, 1)

print(max_cnt[0] + max_cnt[1])