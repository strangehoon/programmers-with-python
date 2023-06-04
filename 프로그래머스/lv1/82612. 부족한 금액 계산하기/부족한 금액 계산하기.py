def solution(price, money, count):

    answer = 0
    list = []
    for i in range(1, count+1):
        list.append(price*i)
    if money >= sum(list):
        return 0
    else:
        return sum(list)-money