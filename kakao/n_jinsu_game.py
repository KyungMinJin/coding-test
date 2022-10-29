# 2018 kakao blind recruitment
def get_n(n, k):
    answer = ''
    if n == 0:
        return '0'
    while n:
        if n % k == 10:
            answer += 'A'
        elif n % k == 11:
            answer += 'B'
        elif n % k == 12:
            answer += 'C'
        elif n % k == 13:
            answer += 'D'
        elif n % k == 14:
            answer += 'E'
        elif n % k == 15:
            answer += 'F'
        else:
            answer += str(n % k)
        n //= k
    return answer[::-1]


def solution(n, t, m, p):
    answer = ''
    max_cnt = get_n(t, n)
    total = ''.join([get_n(i, n) for i in range(t*m)])
    cur = p - 1

    for i in range(t):
        answer += total[cur]
        cur += m

    return answer
