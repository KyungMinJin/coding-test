# dynamic programming
def solution(m, n, puddles):
    graph = [[0 for i in range(m)] for j in range(n)]
    graph[0][0] = 1

    for i in range(n):
        for j in range(m):
            if [i, j] == [0, 0] or [j+1, i+1] in puddles:
                continue
            elif i == 0:
                graph[i][j] += graph[i][j-1]
            elif j == 0:
                graph[i][j] += graph[i-1][j]
            else:
                graph[i][j] += graph[i-1][j] + graph[i][j-1]

    return graph[-1][-1] % 1000000007
