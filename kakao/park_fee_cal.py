# 2018 blind recruitment park fee cal
import math


def solution(fees, records):
    answer = []
    default_m, d_fee, d_min, m_d = fees

    note = {}
    in_out = set()
    for i in records:
        time, car, park_type = i.split(' ')
        note[car] = []

    for i in records:
        time, car, park_type = i.split(' ')
        h, m = time.split(":")
        if park_type == 'IN':
            note[car].append(60 * int(h) + int(m))
            in_out.add(car)
        else:
            note[car][-1] = 60 * int(h) + int(m) - note[car][-1]
            in_out.remove(car)

    if len(in_out) > 0:
        for i in in_out:
            note[i][-1] = 60 * 23 + 59 - note[i][-1]

    fee = {}

    for car in sorted(note.keys()):
        fee[car] = [sum(note[car])]

    for car in fee:
        for park in fee[car]:
            tmp = 0
            if default_m < park:
                tmp += d_fee + math.ceil((park - default_m) / d_min) * m_d
            else:
                tmp += d_fee
            answer.append(tmp)

    return answer
