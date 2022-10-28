def solution(sizes):
    for idx, s in enumerate(sizes):
        sizes[idx] = [max(s), min(s)]
    x_max, y_max = 0, 0
    for s in sizes:
        if x_max < s[0]:
            x_max = s[0]
        if y_max < s[1]:
            y_max = s[1]

    return x_max * y_max
