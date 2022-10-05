from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
visited = {}
for _ in range(m):
    for _ in range(n):
        for _ in range(m):
            for _ in range(n):
                visited[f'{n}{m}{n}{m}'] = False

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
q = deque()


def init():
    rx, ry, bx, by = 0, 0, 0, 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                rx, ry = i, j
            if board[i][j] == 'B':
                bx, by = i, j
    q.append((rx, ry, bx, by, 1))
    visited[f'{rx}{ry}{bx}{by}'] = True


def move(x, y, dx, dy):
    cnt = 0
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        cnt += 1
        x += dx
        y += dy

    return x, y, cnt


def bfs():
    init()
    while q:
        rx, ry, bx, by, depth = q.popleft()

        if depth > 10:
            break

        for i in range(len(dx)):  # 4 방향에 대해
            next_rx, next_ry, r_cnt = move(rx, ry, dx[i], dy[i])
            next_bx, next_by, b_cnt = move(bx, by, dx[i], dy[i])

            if board[next_bx][next_by] == 'O':
                continue

            if board[next_rx][next_ry] == 'O':
                print(depth)
                return

            if next_bx == next_rx and next_by == next_ry:
                if r_cnt > b_cnt:
                    next_rx -= dx[i]
                    next_ry -= dy[i]
                else:
                    next_bx -= dx[i]
                    next_by -= dy[i]

            if not f'{next_rx}{next_ry}{next_bx}{next_by}' in visited.keys():
                visited[f'{next_rx}{next_ry}{next_bx}{next_by}'] = True
                q.append((next_rx, next_ry, next_bx, next_by, depth+1))

    print(-1)


bfs()
