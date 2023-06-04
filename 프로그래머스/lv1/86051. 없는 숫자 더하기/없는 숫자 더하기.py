def solution(numbers):

    num_set = set(numbers)
    x = [0,1,2,3,4,5,6,7,8,9]
    result = []

    for i in num_set:
        if x.count(i)!=0:
            x.remove(i)

    return sum(x)