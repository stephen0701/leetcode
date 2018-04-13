'''
Topic:
    Merged Intervals

Description:
    Given a collection of intervals, merge all overlapping intervals.

Example:
    Given [1,3],[2,6],[8,10],[15,18],
    return [1,6],[8,10],[15,18].
'''

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    
    # Solution: Sort the intervals and merge them if necessary.
    # Time Complexity: O(NlogN) since we sort the intervals first, but Comparision only takes O(N).
    # Space Complexity: O(N), the space for storing the result.
    def merge(self, intervals):
        
        # Sort the intervals list by its start number
        intervals.sort(key=lambda x: x.start)
        
        # Merge the intervals if the start number of current interval is smaller than the end number of last interval
        result = list()
        for interval in intervals:
            if not result or result[-1].end < interval.start:
                result.append(interval)
            else:
                result[-1].end = max(result[-1].end, interval.end)
        return result