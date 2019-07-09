def solution(A:list):
    # write your code in Python 3.6
    A.sort()
    n = 1
    for i in A:
        if i == n:
            n += 1
            continue
        else:
            return 0

    return 1



print(solution( [4, 1, 3, 2]))
print(solution( [4, 1, 3]))