'''
Topic:
    Generate Parentheses

Description:
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example: 
    For example, given n = 3, a solution set is:
    [
      "((()))",
      "(()())",
      "(())()",
      "()(())",
      "()()()"
    ]
'''

class Solution:
    """
    :type n: int
    :rtype: List[str]
    """
    # Solution: Use Recursion algorithm to generate all parentheses case.
    def generateParenthesis(self, n):
        def generate(parens, left, right):
            if(left==n and right==n):
                result.append(parens)
            
            if(left>right):
                generate(parens+")", left, right+1)
            if(left<n):
                generate(parens+"(", left+1, right)
        
        result = []
        if (n<0):
            return result
        
        generate("", 0, 0)
        return result