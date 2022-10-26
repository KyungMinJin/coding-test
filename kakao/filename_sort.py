# 2018 blind recruitment filename sort
def solution(files):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    answer = []

    for i_idx, i in enumerate(files):
        left, right = 0, 0
        chk, chk_tail = 0, 0
        for idx, j in enumerate(i):
            if j in numbers and chk == 0:
                left = idx
                chk = 1
            if j not in numbers and chk == 1 and chk_tail == 0:
                right = idx
                chk_tail = 1
            if idx == len(i) - 1 and chk_tail == 0:
                answer.append([i[:left], i[left:len(i)], ''])

        if chk_tail == 1:
            answer.append([i[:left], i[left:right], i[right:]])

    answer.sort(key=lambda x: (x[0].lower(), int(x[1])))
    for idx, i in enumerate(answer):
        answer[idx] = ''.join(i)

    return answer
