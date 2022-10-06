from sys import stdin
from collections import deque

input = stdin.readline
n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

score = [[0]*m for _ in range(n)]
q = deque()
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)  # 왼, 아래, 오른, 위

# 칸 별 점수
for i in range(n):
    for j in range(m):
        visited = [[0]*m for _ in range(n)]
        score[i][j] += board[i][j]
        # bfs
        q.append((i, j, 1))  # x y depth
        visited[i][j] = 1
        while q:
            x, y, depth = q.popleft()

            for direction in range(len(dx)):
                if 0 <= x+dx[direction] < n and 0 <= y+dy[direction] < m \
                    and board[i][j] == board[x+dx[direction]][y+dy[direction]]\
                        and visited[x+dx[direction]][y+dy[direction]] == 0:  # 연속 칸이고 방문 x 경우
                    q.append((x+dx[direction], y+dy[direction], depth+1))
                    score[i][j] += board[x+dx[direction]][y+dy[direction]]
                    visited[x+dx[direction]][y+dy[direction]] = 1

# 주사위 굴리기
dice = [[0, 2, 0], [4, 1, 3], [0, 5, 0], [0, 6, 0]]


def east(dice):
    return [[0, dice[0][1], 0], [dice[3][1], dice[1][0], dice[1][1]],
            [0, dice[2][1], 0], [0, dice[1][2], 0]]


def west(dice):
    return [[0, dice[0][1], 0], [dice[1][1], dice[1][2], dice[3][1]],
            [0, dice[2][1], 0], [0, dice[1][0], 0]]


def south(dice):
    return [[0, dice[3][1], 0], [dice[1][0], dice[0][1], dice[1][2]],
            [0, dice[1][1], 0], [0, dice[2][1], 0]]


def north(dice):
    return [[0, dice[1][1], 0], [dice[1][0], dice[2][1], dice[1][2]],
            [0, dice[3][1], 0], [0, dice[0][1], 0]]


def get_direction(dice, pos_b, board, direction):
    if dice[3][1] > board[pos_b[0]][pos_b[1]]:
        if direction == 'east':
            return 'south'
        elif direction == 'south':
            return 'west'
        elif direction == 'west':
            return 'north'
        elif direction == 'north':
            return 'east'
    elif dice[3][1] < board[pos_b[0]][pos_b[1]]:
        if direction == 'east':
            return 'north'
        elif direction == 'north':
            return 'west'
        elif direction == 'west':
            return 'south'
        elif direction == 'south':
            return 'east'
    else:
        return direction


direction = 'east'
pos = [0, 0]
idx = 0
res = 0
while idx < k:
    if direction == 'east':
        if pos[1] + 1 >= m:
            direction = 'west'
            continue
        else:
            pos[1] += 1
            dice = east(dice)
            res += score[pos[0]][pos[1]]
            direction = get_direction(dice, pos, board, direction)
            idx += 1
    elif direction == 'west':
        if pos[1] - 1 < 0:
            direction = 'east'
            continue
        else:
            pos[1] -= 1
            dice = west(dice)
            res += score[pos[0]][pos[1]]
            direction = get_direction(dice, pos, board, direction)
            idx += 1
    elif direction == 'south':
        if pos[0] + 1 >= n:
            direction = 'north'
            continue
        else:
            pos[0] += 1
            dice = south(dice)
            res += score[pos[0]][pos[1]]
            direction = get_direction(dice, pos, board, direction)
            idx += 1
    else:
        if pos[0] - 1 < 0:
            direction = 'south'
            continue
        else:
            pos[0] -= 1
            dice = north(dice)
            res += score[pos[0]][pos[1]]
            direction = get_direction(dice, pos, board, direction)
            idx += 1

print(res)
