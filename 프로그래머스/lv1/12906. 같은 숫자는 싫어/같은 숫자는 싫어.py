def solution(arr):
    stack = []
    for i in arr:
        # stack에 push
        if len(stack)==0 or stack[-1] != i:
            stack.append(i)

    return stack