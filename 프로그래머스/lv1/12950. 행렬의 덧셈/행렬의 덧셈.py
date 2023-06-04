def solution(arr1, arr2):

    result = []
    for i in range(len(arr1)):
        x = []
        for j in range(len(arr1[0])):
            x.append(arr1[i][j]+arr2[i][j])
        result.append(x)
    return result
