def solution(n):
    x = bin(n)[2:]
    x_count = x.count('1')
    flag = n + 1
    while(True):
        if(x_count == bin(flag)[2:].count('1')):
            break
        flag +=1
    return flag