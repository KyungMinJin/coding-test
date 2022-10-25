def decode(arr, n):
    res = ["" for _ in arr]
    for idx, a in enumerate(arr):
        for _ in range(n):
            if a % 2 == 1:
                res[idx] = "1" + res[idx]
                a -= 1
                a //= 2
            else:
                res[idx] = "0" + res[idx]
                a //= 2

    return res

def solution(n, arr1, arr2):
    answer = ["" for _ in range(n)]
    d_1 = decode(arr1, n)
    d_2 = decode(arr2, n)
    
    for i in range(n):
        for j in range(n):
            if d_1[i][j] == '1' or d_2[i][j] == '1':
                answer[i] += "#"
            else:
                answer[i] += " "
            
            
    return answer