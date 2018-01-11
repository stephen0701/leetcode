class Solution:
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # Solution 1: Simplest Solution - Loop the list from the start to the end.
    # Testcase Runtime: 74ms
    # Time complextiy: O(n)
    def searchInsert_1(self, nums, target):
        if not nums:
            return 0
        i = 0
        for num in nums:
            if num >= target:
                return i
            else:
                i += 1
        return i
        
    # Solution 2: Binary Search from the middle of the list
    # Testcase Runtime: 67 ms (unknown reason that the solution is not much faster than first one)
    # Time complextiy: O(log n)
    def searchInsert_2(self, nums, target):
        
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = int((low + high) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low
        
    # Solution 3: Most elegent solution
    # Testcase Runtime: 60 ms
    # Time complextiy: O(n)
    def searchInsert_2(self, nums, target):
        return len([x for x in nums if x<target])