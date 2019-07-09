def solution(A):
    # write your code in Python 3.6
    sum_left = 0
    sum_right = 0
    sum_begin = sum(A)
    min_diff = -1
    for num, a in enumerate(A[:-1]):
        print('num ', num, sum_begin)
        if num == 0:
            sum_right = sum_begin - a
            sum_left = a
        else:
            sum_left += a
            sum_right -= a
        print(f'right = {sum_right} left = {sum_left}')
        dif = abs(sum_left - sum_right)
        print(dif)
        if min_diff == -1 or dif < min_diff:
            min_diff = dif
    min_diff = max(0, min_diff)
    return min_diff

print(solution([3, 1, 2, 4, 3]))
print(solution([1, 1]))
print(solution([1, 2]))
print(solution([-1000, 1000]))
