"""
Topic:
    Valid Palindrome
Description:
    Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Example:
    "A man, a plan, a canal: Panama" is a palindrome.
    "race a car" is not a palindrome.
    Empty string is a palindrome.
"""
class Solution:
    """
    :type s: str
    :rtype: bool
    """

    # Solution: Use two variable to find the characters from the leftmost and rightmost.
    #           Compare whether they are the same until they overlaps.
    # Time Complexity: O(N)
    def isPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True