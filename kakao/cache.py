# 2018 kakao blind recruitment cache
def solution(cacheSize, cities):
    answer = 0
    cache = []

    for c in cities:
        if cacheSize == 0:
            answer += 5
            continue
        c = c.lower()
        if c in cache:
            cache.remove(c)
            cache.append(c)
            answer += 1
        else:
            if len(cache) == cacheSize:
                cache = cache[1:]
            cache.append(c)
            answer += 5

    return answer
