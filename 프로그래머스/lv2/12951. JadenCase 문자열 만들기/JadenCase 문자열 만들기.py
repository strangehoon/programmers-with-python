def solution(s):

    s_list = list(s)

    flag = 0
    for i in range(len(s_list)):
        # 숫자일 경우
        if s_list[i].isnumeric():
            flag = 1
        # 첫 문자가 알파벳일 경우
        elif s_list[i].isalpha() and flag == 0:
            s_list[i] = s_list[i].upper()
            flag = 1
        # 공백일 경우
        elif s_list[i] == ' ':
            flag = 0
        # 첫 문자가 아닌 알파벳일 경우    
        else:
            s_list[i] = s_list[i].lower()
    result = ''.join(s_list)
    return result
