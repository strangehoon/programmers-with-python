from itertools import combinations, permutations
def solution(number):

    comb = list(combinations(number, 3))
    count = 0
    for i in comb:
        if sum(i) == 0:
            count += 1

    return count
