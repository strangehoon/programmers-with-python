def solution(start, end):

    result = []
    for i in range(end, start+1):
        result.append(i)
    result.sort(reverse=True)
    return result