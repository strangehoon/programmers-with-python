def solution(s):
    s_list = list(s)
    stack = []
    answer = True
    for i in range(len(s)):
        if s_list[i] == '(':
            stack.append(s_list[i])
        elif s_list[i] == ')':
            if len(stack)==0:
                answer = False
                break
            else:
                x = stack.pop()
                if x != '(':
                    answer = False
                    break
    if len(stack) != 0:
        answer = False

    return answer



