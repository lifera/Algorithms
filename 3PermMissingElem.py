def solution(A:[]):
    # write your code in Python 3.6
    if A:
        A.sort()
        print(A)
        buff = 0
        for a in A:
            if buff+1 < a:
                return a-1
            buff = a
        return a+1
    else:
        return 1

print(solution([2,3,1,5]))
print(solution([2,3,1,4]))
print(solution([2,3,5,4]))
print(solution([]))