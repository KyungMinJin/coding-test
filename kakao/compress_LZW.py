dictionary = [chr(ord('A')+i) for i in range(26)]

def solution(msg):
    answer = []
    idx = 0
    while idx < len(msg):
        chk = True
        for iidx in range(len(msg), idx, -1):
            if msg[idx:iidx] in dictionary:
                answer.append(dictionary.index(msg[idx:iidx])+1)
                dictionary.append(msg[idx:iidx+1])
                idx += (iidx - idx)
                chk = False
                break
        if chk:
            dictionary.append(msg[idx:idx+1])
    return answer
