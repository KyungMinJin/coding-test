# game map dijkstra
from collections import deque


def solution(maps):
    queue = deque([(0, 0, 1)])
    n = len(maps)-1
    m = len(maps[0])-1
    visited = [[0 for _ in range(m+1)] for _ in range(n+1)]

    while queue:
        i, j, cnt = queue.popleft()
        if i == n and j == m:
            return cnt
#         if visited[i][j] == 0 or visited[i][j] > cnt: # 업데이트 해줄 필요 없음 bfs라 먼저 도착
#             visited[i][j] = cnt

#         if visited[n][m] > 0:
#             return visited[n][m]
        # left
        if i - 1 >= 0 and visited[i-1][j] == 0 and maps[i-1][j] == 1:
            queue.append((i-1, j, cnt+1))
            visited[i-1][j] = 1
        # right
        if i + 1 <= n and visited[i+1][j] == 0 and maps[i+1][j] == 1:
            queue.append((i+1, j, cnt+1))
            visited[i+1][j] = 1
        # top
        if j - 1 >= 0 and visited[i][j-1] == 0 and maps[i][j - 1] == 1:
            queue.append((i, j-1, cnt+1))
            visited[i][j-1] = 1
        # bottom
        if j + 1 <= m and visited[i][j+1] == 0 and maps[i][j + 1] == 1:
            queue.append((i, j+1, cnt+1))
            visited[i][j+1] = 1

    return -1
