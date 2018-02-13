"""
Topic: 
    Longest Substring Without Repeating Characters
Description:
    Given a string, find the length of the longest substring without repeating characters.
"""

class Solution:
    """
    :type s: str
    :rtype: int
    """
    # Solution 1: Use a string variable to store current longest string. 
    #             If a repeating char appears, compare the length with the max length.
    #             Update the string variable.
    # Time Complexity: O(n^2) since the time complexity of searching in a list is O(n), it can be faster by replacing the list with a hash map.
    # Space Complexity: O(n)
    def lengthOfLongestSubstring(self, s):
        max_length, length = 0, 0
        sub = ""
        for c in s:
            if c in sub:
                sub = sub[sub.index(c)+1:] + c
                length = len(sub)
            else:
                sub += c
                length += 1
                max_length = max(length, max_length)
                
        return max_length
        
    # Solution 2: Use a Hash Map to store the place of appearing char and an int variable to store the current starting index.
    #             If a repeating char appears after the current starting index, compare the current substring length with the max length.
    #             Update the index of the repeating char in the Hash Map.
    # Time Complexity: O(n) since the searching operation in a map is O(1)
    # Space Complexity: O(n)
    def lengthOfLongestSubstring_2(self, s):
        start, max_length = 0, 0
        char_map = {}
        for idx, c in enumerate(s):
            if c in char_map and char_map[c] >= start:
                start = char_map[c]+1
            char_map[c] = idx
            max_length = max(max_length, idx-start+1)
        return max_length