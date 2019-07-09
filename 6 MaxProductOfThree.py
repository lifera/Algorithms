'''
A non-empty array A consisting of N integers is given. The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).

For example, array A such that:
  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6

contains the following example triplets:

        (0, 1, 2), product is −3 * 1 * 2 = −6
        (1, 2, 4), product is 1 * 2 * 5 = 10
        (2, 4, 5), product is 2 * 5 * 6 = 60

Your goal is to find the maximal product of any triplet.

Write a function:

    def solution(A)

that, given a non-empty array A, returns the value of the maximal product of any triplet.

For example, given array A such that:
  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6

the function should return 60, as the product of triplet (2, 4, 5) is maximal.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [3..100,000];
        each element of array A is an integer within the range [−1,000..1,000].
'''

def solution(A:[]) -> int:
    # write your code in Python 3.6
    max_1, max_2, max_3, result = 0, 0, 0, 0
    len_a = len(A)
    for p in range(len_a-2):
        for q in range(p+1, len_a-1):
            for r in range(q+1, len_a):
                result = max(result, A[p]*A[q]*A[r])
    return result

def solution2(A:[]) -> int:
    # write your code in Python 3.6
    A.sort()
    return max(A[0]*A[1]*A[-1], A[-3]*A[-2]*A[-1])

print(solution2([-3, 1, 2, -2, 5, 6]))
print(solution2([-3, 1, 2, -2, 5, 6, -7]))