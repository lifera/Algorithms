'''

A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:
    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2

we can find two equi leaders:

        0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
        2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.

The goal is to count the number of equi leaders.

Write a function:

    def solution(A)

that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

For example, given:
    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2

the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].

'''

def solution(A):
    # write your code in Python 3.6
    equi_leader = 0
    size = 0
    value = 0
    for a in A:
        if not size:
            value = a
            size += 1
        else:
            if value == a:
                size += 1
            else:
                size -= 1

    if size > 0:
        candidate = value
        total_candidates = A.count(candidate)

        pref_sum = 0
        for index, a in enumerate(A):
            if a == candidate:
                total_candidates -= 1
                pref_sum += 1
            if pref_sum > (index+1)//2:
                if total_candidates > (len(A)-(index+1))//2:
                    equi_leader += 1

    return equi_leader


print(solution([4, 3, 4, 4, 4, 2]))