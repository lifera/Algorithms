''''''
def solution(N, A):
    # write your code in Python 3.6
    n = [0]*N
    max_n, min_n = 0, 0
    for i in A:
        if i == N + 1:
            min_n = max_n
            print(n)
        else:
            n[i-1] = max(min_n+1, n[i-1]+1)
            max_n = max(max_n, n[i-1])
        print(i, n)
    for num, i in enumerate(n):
        n[num] = max(min_n, n[num])
    return n

print(solution(5, [3, 4, 4, 6, 1, 4, 4]))