# minimum spanning tree
# kruskal
# greedy
def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]

def union_parent(parents, x, y):
    x = find_parent(parents, x)
    y = find_parent(parents, y)
    if x < y:
        for idx, i in enumerate(parents):
            if i == y:
                parents[idx] = x
    else:
        for idx, i in enumerate(parents):
            if i == x:
                parents[idx] = y
        
def solution(n, costs):
    answer = 0
    parents = [i for i in range(n)]
    costs.sort(key= lambda x: (x[2]))

    for i in costs:
        x, y, cost = i
        if find_parent(parents, x) != find_parent(parents, y):
            union_parent(parents, x, y)
            answer += cost

    return answer
       