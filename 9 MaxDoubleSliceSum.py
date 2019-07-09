'''

A non-empty array A consisting of N integers is given.

A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.

The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

For example, array A such that:
    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2

contains the following example double slices:

        double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
        double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
        double slice (3, 4, 5), sum is 0.

The goal is to find the maximal sum of any double slice.

Write a function:

    def solution(A)

that, given a non-empty array A consisting of N integers, returns the maximal sum of any double slice.

For example, given:
    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2

the function should return 17, because no double slice of array A has a sum of greater than 17.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [3..100,000];
        each element of array A is an integer within the range [−10,000..10,000].

'''


def solution(A):
    # write your code in Python 3.6
    n = len(A)
    max_double_slice_sum = 0
    current_double_slice_sum = 0
    current_left_slice_sum = 0
    for z in range(3, n):
        current_left_slice_sum = max(0, current_left_slice_sum + A[z - 2])
        current_double_slice_sum = max(current_double_slice_sum + A[z - 1], current_left_slice_sum)
        max_double_slice_sum = max(max_double_slice_sum, current_double_slice_sum)
        print(f'z = {z}, a = { A[z-1]}, current_left_slice_sum={current_left_slice_sum}, current_double_slice_sum={current_double_slice_sum}, max_double_slice_sum={max_double_slice_sum}')
    return max_double_slice_sum


def solution2(A):
    # write your code in Python 3.6
    n = len(A)
    max_slice_ending_here = [0]
    max_slice_starting_here = [0]
    slice_ending_here = slice_starting_here = 0
    for a in A[1:-2]:
        slice_ending_here = max(slice_ending_here + a, 0)
        max_slice_ending_here.append(max(max_slice_ending_here[-1], slice_ending_here))
        print(max_slice_ending_here)

    for index, a in enumerate(A[-2:1:-1]):
        slice_starting_here = max(slice_starting_here + a, 0)
        max_slice_starting_here.append(max(max_slice_starting_here[-1], slice_starting_here))
        print(max_slice_starting_here, index)

    print(max_slice_ending_here)
    print(max_slice_starting_here)

    for i in range(1, n-2):
        print(max_slice_starting_here[i+2], max_slice_ending_here[i])

    return max_slice_ending_here



print(solution2([3, 2, 6, -1, 4, 5, -1, 2]))
print(solution2([-3, -2, -6, -1, -4, -5, -1, 2]))