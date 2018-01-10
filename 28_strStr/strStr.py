class Solution:
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    # Testcase Runtime: 61ms
    def strStr_1(self, haystack, needle):
        if len(needle) == 0:
            return 0
        elif len(needle) > len(haystack):
            return -1
        
        for i, char in enumerate(haystack):
            if i+len(needle) > len(haystack):
                break
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
    
    # Testcase runtime: 66ms
    def strStr_2(self, haystack, needle):
        return haystack.find(needle)