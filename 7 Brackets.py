'''

A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

        S is empty;
        S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
        S has the form "VW" where V and W are properly nested strings.

For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

    def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..200,000];
        string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".

'''

def solution2(S):
    # write your code in Python 3.6
    opened1, opened2, opened3 = 0, 0, 0

    if not S:
        return 1

    a = ''
    for s in S:

        if s == '(':
            opened1 += 1
        elif s == '{':
            opened2 += 1
        elif s == '[':
            opened3 += 1
        elif s == ')' and a != '[' and a != '{':
            opened1 -= 1
        elif s == '}' and a != '[' and a != '(':
            opened2 -= 1
        elif s == ']' and a != '(' and a != '{':
            opened3 -= 1

        if opened1 < 0 or opened2 < 0 or opened3 < 0:
            return 0
        a = s
    if opened1 == 0 and opened2 == 0 and opened3 == 0:
        return 1
    else:
        return 0

def solution(S):
    if not S:
        return 1

    stack = []
    to_push = ['[', '{', '(']
    to_pop = {']' : '[', '}' : '{', ')' : '('}

    for s in S:
        if s in to_push:
            stack.append(s)
        else:
            if not stack or stack.pop() != to_pop[s]:
                return 0
    if len(stack) == 0:
        return 1
    else:
        return 0


print(solution('{[()()]}'))
print(solution('([)()]'))