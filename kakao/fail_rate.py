# 2019 blind recruitment fail rate
def solution(N, stages):
    cnt = [0 for i in range(N+1)]

    for s in stages:
        if s > N:
            cnt[-1] += 1
        if s <= N:
            cnt[s-1] += 1

    c = [[0 if cnt[i] == 0 else cnt[i] / sum(cnt[i:]), i+1] for i in range(N)]
            
    c.sort(key= lambda x: (x[0]), reverse=True)
    for i in range(N):
        c[i] = c[i][1]
        
    return c