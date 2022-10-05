from sys import stdin

input = stdin.readline
n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

road = 0
# 가로
for i in range(n):
    slope_board = [[0]*n for _ in range(n)]
    for j in range(n-1):
        flag = False

        if board[i][j] < board[i][j+1]:
            for k in range(l):
                if j-k < 0 or board[i][j+1] - board[i][j-k] != 1 or slope_board[i][j-k] == 1:
                    flag = True
            if not flag:
                for k in range(l):
                    slope_board[i][j-k] = 1
        elif board[i][j] > board[i][j+1]:
            for k in range(l):
                if j+1+k >= n or board[i][j+1+k] - board[i][j] != -1 or slope_board[i][j+1+k] == 1:
                    flag = True
            if not flag:
                for k in range(l):
                    slope_board[i][j+1+k] = 1

        if flag:
            break

    if not flag:
        road += 1

# 세로
for i in range(n):
    slope_board = [[0]*n for _ in range(n)]
    for j in range(n-1):
        flag = False

        if board[j][i] < board[j+1][i]:
            for k in range(l):
                if j-k < 0 or board[j+1][i] - board[j-k][i] != 1 or slope_board[j-k][i] == 1:
                    flag = True
            if not flag:
                for k in range(l):
                    slope_board[i][j-k] = 1
        elif board[j][i] > board[j+1][i]:
            for k in range(l):
                if j+1+k >= n or board[j+1+k][i] - board[j][i] != -1 or slope_board[j+1+k][i] == 1:
                    flag = True
            if not flag:
                for k in range(l):
                    slope_board[j+1+k][i] = 1

        if flag:
            break

    if not flag:
        road += 1

print(road)
