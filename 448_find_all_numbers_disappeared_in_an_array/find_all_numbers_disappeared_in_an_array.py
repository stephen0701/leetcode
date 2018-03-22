"""
Topic: 
    Find All Numbers Disappeared in an Array
Description:
    Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
    Find all the elements of [1, n] inclusive that do not appear in this array.
    
Note:
    The question could be solved at time complexity of O(N) and without using extra memory.
"""

class Solution:
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # Solution 1: Use a list to record whether the element appears or not.
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    def findDisappearedNumbers(self, nums):
        shown = [0]*len(nums)
        for n in nums:
            shown[n-1] = 1
        
        result = list()
        for i in range(len(appear)):
            if shown[i] == 0:
                result.append(i+1)
        return result
        
    # Solution 2: In 1st iteration, mark the element, which index is the numbers have shown, as negative.
    #             In 2nd iteration, append the indice which element is positive in the result.
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def findDisappearedNumbers(self, nums):

        for n in nums:
            idx = abs(n)-1
            nums[idx] = - abs(nums[idx])

        return [ i+1 for i in range(len(nums)) if nums[i]>0]