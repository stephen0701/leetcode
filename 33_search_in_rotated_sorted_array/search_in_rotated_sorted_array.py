'''
Topic:
    Search in Rotated Sorted Array
    
Description:
    Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
    You are given a target value to search.
    If it is found in the array return its index, otherwise return -1.
    
Note:
    You may assume no duplicate exists in the array.
'''
class Solution:
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # Solution: Use binary search with condition that keeps the search index moving in a correct direction.
    # Time Complexity: O(logN)
    # Space Complexity: O(1)
    def search(self, nums, target):
        start, end = 0, len(nums)-1
        while(start<=end):
            mid = int((start+end)/2)
            if target > nums[mid]:
                if nums[mid] < nums[0] <= target:
                    end = mid-1
                else:
                    start = mid+1
            elif target < nums[mid]:
                if nums[mid] >= nums[0] > target:
                    start = mid+1
                else:
                    end = mid-1
            else:
                return mid
        return -1