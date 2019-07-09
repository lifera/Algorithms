'''

We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).

The figure below shows discs drawn for N = 6 and A as follows:
  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0

There are eleven (unordered) pairs of discs that intersect, namely:

        discs 1 and 4 intersect, and both intersect with all the other discs;
        disc 2 also intersects with discs 0 and 3.

Write a function:

    def solution(A)

that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

Given array A shown above, the function should return 11, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..100,000];
        each element of array A is an integer within the range [0..2,147,483,647].

'''


def solution(A):
    result = 0
    for a in range(len(A)-1):
        for b in range(a+1, len(A)):
            if (A[a] + A[b]) >= (b - a):
                result += 1
                print(A[a], A[b], a, b)
                if result >= 10000000:
                    return -1
    return result

def solution2(A):
    result = 0
    len_A = len(A)
    low_limits, high_limits = [], []
    for index, a in enumerate(A):
        low_limits.append(index - a)
        high_limits.append(index + a)

    low_limits.sort()
    high_limits.sort()
    print(low_limits, high_limits)
    low_index = 0
    for high_index in range(0, len_A):
        while low_index < len_A\
                and high_limits[high_index] >= low_limits[low_index]:
            low_index += 1

        result += low_index - high_index - 1
        if result >= 10000000:
            return -1
    return result


print(solution2([1, 5, 2, 1, 4, 0]))
print(solution2([]))