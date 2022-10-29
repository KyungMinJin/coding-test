def solution(word):
    alpha = ['', 'A', 'E', 'I', 'O', 'U']
    dic = set()
    for i in alpha:
        for j in alpha:
            for k in alpha:
                for l in alpha:
                    for m in alpha:
                        dic.add(f'{i}{j}{k}{l}{m}')

    dic = sorted(list(dic))
    dic.remove('')  # 빈 문자열 첫 하나밖에 없음

    return dic.index(word) + 1
