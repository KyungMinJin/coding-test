# 2022 kakao tech internship
def solution(queue1, queue2):
    q = queue1 + queue2
    i, j, cnt = 0, len(queue1), 0
    curr = sum(queue1)
    target = sum(q) // 2

    while i < len(q) and j < len(q):
        if curr == target:
            return cnt
        elif curr < target and j+1 < len(q):
            curr += q[j]
            j += 1
            cnt += 1
        else:
            curr -= q[i]
            i += 1
            cnt += 1

    return -1
