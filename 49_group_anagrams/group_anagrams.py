'''

Topic:
    Group Anagrams

Description:
    Given an array of strings, group anagrams together.

For example:

Given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:
    [
      ["ate", "eat","tea"],
      ["nat","tan"],
      ["bat"]
    ]

Note:
    All inputs will be in lower-case.

'''


class Solution:
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """

    # Solution 1: Compare each word by sorting its characters and store them into a dictionary which key is the sorted string.
    # Time Complexity: O(N*KlogK) where N is the length of strs and K is the maximum word length.
    # Space Complexity: O(N*K)
    def groupAnagrams_1(self, strs):
        ans = collections.defaultdict(list)
        for word in strs:
            # the type of the keys can be string or tuple
            anagram = ''.join(c for c in sorted(word))
            ans[anagram].append(word)

        return list(ans.values())

    # Solution 2: Convert each word into an array of characters' count first.
    #             Store them into a dictionary where the keys are the tuple of the count array.
    # Time Complexity: O(N*K)
    # Space Complexity: O(N*K)
    def groupAnagrams_2(self, strs):

        ans = collections.defaultdict(list)
        for word in strs:
            count = [0]*26
            for c in word:
                count[ord(c)-ord('a')]+=1
            ans[tuple(count)].append(word)
        return list(ans.values())