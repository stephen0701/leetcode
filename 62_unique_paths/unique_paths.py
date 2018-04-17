'''
    Topic:
        Unique Paths

    Description:
        A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
        The robot can only move either down or right at any point in time.
        The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
        How many possible unique paths are there?

    Note:
        m and n will be at most 100.

    Example:
        (Example 1)
        Input: m = 3, n = 2
        Output: 3
        Explanation:
        From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
        1. Right -> Right -> Down
        2. Right -> Down -> Right
        3. Down -> Right -> Right

        (Example 2)
        Input: m = 7, n = 3
        Output: 28

'''

class Solution:
    """
    :type m: int
    :type n: int
    :rtype: int
    """

    # Solution 1: Use Dynamic Programming method.
    # Time Complexity: O(m*n)
    # Space Complexity: O(m*n)
    def uniquePaths_1(self, m, n):

        p = [[1]*n]*m
        for i in range(1, m):
            for j in range(1, n):
                p[i][j] = p[i-1][j] + p[i][j-1]
        return p[m-1][n-1]

    # Solution 2: Use Dynamic Programming with elegance and brevity
    # Time Complexity: O(m*n)
    # Space Complexity: O(m or n), which depends on which is shorter.
    def uniquePaths_2(self, m, n):

        p = [1] * m
        # Inverse the matrix if rows are more than columns to save the space
        if m > n:
            return self.uniquePaths_1(n, m)

        for i in range(1, n):
            for j in range(1, m):
                p[j] += p[j - 1]
        return p[m - 1]

    # Note: Other methods are available,
    # such as using math probability formula or two list to store the vaules for the current column and the previous column