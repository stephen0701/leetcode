'''
Topic:
Letter Combination of a Phone Number

Description:
Given a digit string, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below.

For example:
Input = "23"
Output = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
The answer could be in any order, no need to be in lexicographical order.
'''


class Solution:
    """
    :type digits: str
    :rtype: List[str]
    """

    # Solution 1: Use for loop to find all the possible combinations. It can also be done using recursive method.
    # Time Complexity: O(r^N) where r is the longest string in mapping dictionary, say 4 in this case,
    #                           and N is the length of the digits
    # Space Complexity: O(r^N) since the result will have at most r^N combinations.
    # Note: the Time Complexity is a geometric sequence problem, time = r+r^2+r^3+...+r^N
    def letterCombinations_1(self, digits):

        mapping = {"2": "abc",
                   "3": "def",
                   "4": "ghi",
                   "5": "jkl",
                   "6": "mno",
                   "7": "pqrs",
                   "8": "tuv",
                   "9": "wxyz"}

        cand = [""] if len(digits) else []
        for d in digits:
            result = []
            for c in mapping[d]:
                for s in cand:
                    result.append(s + c)
            cand = result
        return result

    # Solution 2: similar but cleaner solution to Solution 1
    def letterCombinations_2(self, digits):

        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = [""] if len(digits) else []
        for d in digits:
            result = [s + a for a in mapping[d] for s in result]
        return result