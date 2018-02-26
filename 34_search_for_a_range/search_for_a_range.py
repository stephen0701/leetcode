'''
Topic:
    Search for a Range

Description:
    Given an array of integers sorted in ascending order, 
    find the starting and ending position of a given target value.
    Runtime complexity must be in the order of O(log n).
    If the target is not found in the array, return [-1, -1].

Example: 
    Given [5, 7, 7, 8, 8, 10] and target value 8,
    return [3, 4].
'''

class Solution:
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """   
    # Solution 1: First, add dummy value at the front and the end to handle the corner cases.
    #             Use Divide and Conquer algorithm.
    #             Find the answer by comparing the current index and its neighboring index.
    # Time Complexity: O(log N)
    # Space Complexity: O(1)
    def searchRange_1(self, nums, target):

        start, end = -1, -1        
        nums.insert(0, float('-inf'))
        nums.insert(len(nums), float('inf'))
        left, right= 0, len(nums)-1
        
        # Find the start idx of the target
        while(left<=right):
            middle = int((left+right)/2)
            if(nums[middle]==target and nums[middle-1]<target):     
                start = middle-1
                break
            elif(nums[middle]>target or nums[middle]==target):
                right = middle-1
            else:
                left = middle+1
          
        # Find the end idx of the target
        left, right = 0, len(nums)-1
        while(left<=right):
            middle = int((left+right)/2)
            if(nums[middle]==target and nums[middle+1]>target):
                end = middle-1
                break
            elif(nums[middle]>target):
                right = middle-1
            else:
                left = middle+1
        
        return [start, end]
    
    # Solution 1: Use the Divide and Conquer algorithm with minor difference.
    #             Find the answer by halving the range until it reaches the only one possible answer.
    # Time Complexity: O(log N)
    # Space Complexity: O(1)
    def searchRange_2(self, nums, target):
        
        if(len(nums)<=0):
            return [-1, -1]
        
        start, end = -1, -1        
        left, right= 0, len(nums)-1
        
        # Find the start idx of the target
        while(left<right):
            middle = int((left+right)/2)
            if(nums[middle]>=target):     
                right = middle
            else:
                left = middle+1
        if(nums[left]!=target):
            return [-1, -1]
        else:
            start = left

        # Find the end idx of the target
        left, right = 0, len(nums)-1
        while(left<right):
            middle = int((left+right)/2)+1
            if(nums[middle]<=target):
                left = middle
            else:
                right = middle-1
        end = left
        return [start, end]