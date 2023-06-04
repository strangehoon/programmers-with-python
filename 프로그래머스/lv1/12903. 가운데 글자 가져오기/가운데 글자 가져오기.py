def solution(s):

    length = len(s)
    # 홀수
    if length%2 != 0:
        return s[length//2]
    # 짝수    
    else:
        return s[length//2-1:length//2+1]