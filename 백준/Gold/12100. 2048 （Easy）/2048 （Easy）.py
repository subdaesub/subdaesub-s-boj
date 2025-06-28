dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

max_block = max(map(max, board))

def move(board, direction):
    new_board = [[0] * n for _ in range(n)]

    for i in range(n):
        temp = []
        merged = []

        for j in range(n):
            x, y = i, j
            if direction == 0:
                x, y = j, i
            elif direction == 1:
                x, y = n - 1 - j, i
            elif direction == 2:
                x, y = i, j
            elif direction == 3:
                x, y = i, n - 1 - j

            val = board[x][y]
            if val == 0:
                continue

            if temp and temp[-1] == val and not merged[-1]:
                temp[-1] *= 2
                merged[-1] = True
            else:
                temp.append(val)
                merged.append(False)

        for j in range(len(temp)):
            x, y = i, j
            if direction == 0:
                new_board[j][i] = temp[j]
            elif direction == 1:
                new_board[n - 1 - j][i] = temp[j]
            elif direction == 2:
                new_board[i][j] = temp[j]
            elif direction == 3:
                new_board[i][n - 1 - j] = temp[j]

    return new_board

def dfs(board, cnt):
    global max_block
    if cnt == 5:
        for row in board:
            max_block = max(max_block, max(row))
        return

    for dir in range(4):
        next_board = move(board, dir)
        if next_board != board:
            dfs(next_board, cnt + 1)

dfs(board, 0)
print(max_block)