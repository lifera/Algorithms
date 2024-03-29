'''

Write a function:

    def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

    { i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

        A and B are integers within the range [0..2,000,000,000];
        K is an integer within the range [1..2,000,000,000];
        A ≤ B.

'''

def solution(A:int, B:int, K:int) -> int:
    # write your code in Python 3.6
    count_div = 0
    for i in range(A, B+1):
        if i % K == 0:
            count_div += 1
    return count_div

def solution2(A:int, B:int, K:int) -> int:
    # write your code in Python 3.6
    count_div = (B - (A - A%K))//K
    if A % K == 0:
        return count_div+1
    else:
        return count_div

print(solution2(6, 11, 2))
print(solution2(11, 345, 17))
print(solution2(0, 0, 17))