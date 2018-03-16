'''
Topic:
Longest Palindromic Substring

Description:
Given a string s, find the longest palindromic substring in s.

For example:
Input = "babad"
Output = "bab" or "aba"

Input = "cbbd"
Output = "bb"

Note:
You may assume that the maximum length of s is 1000.
'''


class Solution:
    """
    :type s: str
    :rtype: str
    """
    # Solution 1: Assume each character in the string as the center of a palindromic string.
    #             Find its longest palindromic string and compare it with current longest answer.
    # Time Complexity: O(N^2)
    # Space Complexity: O(1)
    def longestPalindrome_1(self, s):

        result = ""
        for mid in range(len(s)):
            # Handle even palindromic case, say "abba"
            sub = self.maxPalindrome(s, mid, mid + 1)
            result = sub if len(sub) > len(result) else result

            # Handle odd palindromic case, say "aba"
            sub = self.maxPalindrome(s, mid, mid)
            result = sub if len(sub) > len(result) else result
        return result

    # Helper function for solution 1
    def maxPalindrome(self, s, l, r):
        while l > -1 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

    # Solution 2: Determine if the string is a longer palindrome when adding a new character at the end.
    # Time Complexity: O(k*N) or O(N) depends the time complexity of string comparison, slicing and reverse,
    #                  and k = length of longest substring here.
    # Space Complexity: O(1)
    # Note:
    # (1) Time complexity of string comparison in Python is O(1) since string is immutable in Python
    # (2) Time complexity of string slicing and reverse seems to be O(N)
    def longestPalindrome_2(self, s):

        maxlen = 0
        start = 0
        for i in range(len(s)):
            if i - maxlen >= 1 and s[i - maxlen - 1:i + 1] == s[i - maxlen - 1:i + 1][::-1]:
                start = i - maxlen - 1
                maxlen += 2
                continue

            if i - maxlen >= 0 and s[i - maxlen:i + 1] == s[i - maxlen:i + 1][::-1]:
                start = i - maxlen
                maxlen += 1
        return s[start:start + maxlen]

    # There are other solutions like Dynamic Programming Table and Manacher's Algorithm.