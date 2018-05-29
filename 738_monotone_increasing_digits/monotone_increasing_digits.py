'''
Topic:
Monotone Increasing Digits

Description:
Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.
(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y)

Note:
    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

Example:
[1]
    Input: N = 10
    Output: 9
[2]
    Input: N = 1234
    Output: 1234
[3]
    Input: N = 332
    Output: 299
[4]
    Input: N = 223311
    Output: 222999


Note: N is an integer in the range [0, 10^9].
'''


class Solution:
    """
    :type N: int
    :rtype: int
    """
    def monotoneIncreasingDigits(self, N):
        # Note: use string to convert the number to a list of digits, which is easier to handle edge cases
        # For example, input = 100, output = 99
        n = N
        l = [int(num) for num in str(n)]

        # Find the first decreasing occurrence
        i = 0
        while l[i] <= l[i + 1]:
            i += 1

            # N is already a monotone increasing number
            if i == len(l) - 1:
                return N

        # To handle the special case below, move back index i to find the correct digit
        # Input = 332, Output = 299 (not 229)
        while i > 0 and l[i] == l[i - 1]:
            i -= 1

        # Decrease the index i by 1 and correct all the digits after the index to 9
        l[i] -= 1
        for i in range(i + 1, len(l)):
            l[i] = 9

        res = int(''.join([str(num) for num in l]))
        return res