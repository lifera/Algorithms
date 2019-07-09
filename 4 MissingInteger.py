'''Write a function:

    def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [−1,000,000..1,000,000].

'''
def solution(A):
    # write your code in Python 3.6
    A.sort()
    set_A = set([a for a in A if a > 0])
    n = 1
    for a in set_A:
        n += 1
        if a!=n-1:
            return n-1
    return n

def solution2(A):
    z = list(range(1,len(A)+1))
    try:
        result = set(z).difference(set(A)).pop()
    except:
        result = max(A)+1
    return result

print(solution2([1, 3, 6, 4, 1, 2]))
print(solution2([1, 2, 3]))
print(solution2([2]))