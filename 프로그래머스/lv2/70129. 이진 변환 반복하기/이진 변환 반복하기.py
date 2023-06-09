def solution(s):

    answer = []
    # x : 제거된 0의 개수
    x = 0
    # y : 이진 변환의 횟수
    y = 0
    while(s != '1'):
        len_s = len(s)
        s = s.replace('0', '')
        x += len_s - len(s)
        s = bin(len(s))
        s = s[2:]
        y += 1
    answer.append(y)
    answer.append(x)
    return answer