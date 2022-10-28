# 2022 kakao blind recruitment
def check_prime(number):
    if number == '':
        return 0
    number = int(number)
    if number == 1:
        return 0
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return 0
    return 1


def solution(n, k):
    answer = 0

    tmp = ''
    while n:
        tmp = str(n % k) + tmp
        n //= k

    split_tmp = tmp.split('0')

    # 0p0
    if len(split_tmp) > 2:
        a = split_tmp[1:-1]
        for i in a:
            answer += check_prime(i)
    if '0' in tmp:
        # p0
        b = split_tmp[0]
        answer += check_prime(b)
        # 0p
        c = split_tmp[-1]
        answer += check_prime(c)
    # p
    else:
        d = tmp
        answer += check_prime(d)

    return answer
