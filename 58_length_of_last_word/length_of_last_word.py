class Solution:
    """
    :type s: str
    :rtype: int
    """
    # Solution 1: Find the first character from the end and count the length until a space is present
    def lengthOfLastWord_1(self, s):
        count = 0
        for idx in range(len(s)):
            c = s[len(s)-idx-1]
            if c is ' ' and count != 0:
                break
            elif c is ' ' and count == 0:
                continue
            elif c is not ' ':
                count += 1
        return count
    # Solution 2: An elegant solution
    def lengthOfLastWord_2(self, s):
        return len(s.rstrip().split(' ')[-1])