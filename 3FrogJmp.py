def solution(X, Y, D):
    # write your code in Python 3.6
    x = X
    y = Y
    d = D
    # count_of_jumps = 0
    return -(-(y-x)//d)
    # return count_of_jumps

print(solution(3, 999111321, 7))
print(solution(3, 3, 1))
print(solution(10, 85, 30))
