"""
Topic: 
    Climbing Stairs
Description:
    You are climbing a stair case. It takes n steps to reach to the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note:
    Given n will be a positive integer.
"""
class Solution(object):
    """
    :type n: int
    :rtype: int
    """
    # Solution 1: Dynamic Programming with memorization
    # Testcase Runtime: 33ms
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def climbStairs_1(self, n):
        ans = [0, 1, 2]
        for i in range(3, n+1):
            ans.insert(i, ans[i-1]+ans[i-2])
        return ans[n]
    
    # Solution 2: Fibonacci method
    # Testcase Runtime: 32ms
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def climbStairs_2(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        
        first = 1
        second = 2
        for i in range(3, n+1):
            ans = first + second
            
            # Update the series for next round calculation
            first = second
            second = ans
        return ans