class Solution(object):
    """
    :type x: int
    :rtype: int
    """
    # Solution: Use Binary Search from 0 to x since the square root of x must be a number between 0 and x
    # Testcase Runtime: 69ms
    # Note: There are other solution using bit manipulation or Newton's method
    def mySqrt(self, x):
        top, bottom = x, 0
        while True:
            mid = int((top+bottom)/2)
            if mid**2 <= x < (mid+1)**2:
                return mid
            elif mid**2 < x:
                bottom = mid+1
            else:
                top = mid