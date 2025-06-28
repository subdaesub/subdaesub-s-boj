import sys
input = sys.stdin.readline

board = [list(map(int, input().strip())) for _ in range(9)]

row_used = [[False] * 10 for _ in range(9)]
col_used = [[False] * 10 for _ in range(9)]
box_used = [[False] * 10 for _ in range(9)]

empty = []

for i in range(9):
    for j in range(9):
        num = board[i][j]
        if num != 0:
            row_used[i][num] = True
            col_used[j][num] = True
            box_used[(i // 3) * 3 + (j // 3)][num] = True
        else:
            empty.append((i, j))

def solve(idx):
    if idx == len(empty):
        for row in board:
            print("".join(map(str, row)))
        exit()

    x, y = empty[idx]
    box_idx = (x // 3) * 3 + (y // 3)

    for num in range(1, 10):
        if not row_used[x][num] and not col_used[y][num] and not box_used[box_idx][num]:
            board[x][y] = num
            row_used[x][num] = col_used[y][num] = box_used[box_idx][num] = True

            solve(idx + 1)

            board[x][y] = 0
            row_used[x][num] = col_used[y][num] = box_used[box_idx][num] = False

solve(0)