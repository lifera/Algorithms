def solution(X, A):
    # write your code in Python 3.6
    frog = 0
    x = [False]*X
    for num, a in enumerate(A):
        print('num', num)
        x[a-1] = True
        while x[frog]:
            frog += 1
            if frog == X:
                return num
    return -1


print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))