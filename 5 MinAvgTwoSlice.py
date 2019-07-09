'''

A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:
    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8

contains the following example slices:

        slice (1, 2), whose average is (2 + 2) / 2 = 2;
        slice (3, 4), whose average is (5 + 1) / 2 = 3;
        slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.

The goal is to find the starting position of a slice whose average is minimal.

Write a function:

    def solution(A)

that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.

For example, given array A such that:
    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8

the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [2..100,000];
        each element of array A is an integer within the range [−10,000..10,000].

'''

def solution(A:[])->int:
    def pref_sums(Z:[]) -> []:
        P = [0] * (len(Z)+1)
        for p in range(len(Z)):
            P[p+1] = P[p] + Z[p]
        return P

    def slice_avg(prefs: [], left: int, right: int):
        return (prefs[right + 1] - prefs[left])/(right - left + 1)

    prefs = pref_sums(A)
    min_slice_avg = float('inf')
    results = {}
    for a in range(len(A)):
        for b in range(a+1, min(a+5, len(A))):
            print('a b', a, b)
            slice = slice_avg(prefs, a, b)
            if min_slice_avg > slice:
                print('a b', a, b, slice)
                min_slice_avg = slice
                results[min_slice_avg] = a

    result = results[min(results.keys())]

    return result

print(solution([4, 2, 2, 5, 1, 5, 8]))