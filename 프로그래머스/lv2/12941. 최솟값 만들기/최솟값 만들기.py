def solution(A,B):

    A.sort()
    B.sort(reverse=True)
    result = []
    for i in range(len(A)):
        result.append(A[i]*B[i])
    return sum(result)