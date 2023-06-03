def solution(s):
    s_list = s.split(" ")
    new_list = list(map(int, s_list))

    answer = str(min(new_list)) + " " + str(max(new_list))
    return answer