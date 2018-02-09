"""
Topic: 
    Move Zeroes
Description:
    Given an array "nums", move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note:
    ．You must do this in-place without making a copy of the array.
    ．Minimize the total number of operations.
"""

class Solution:
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    # Solution1: Store the pos of zeroes in a list, calculate the corresponding space of moving forward for each element, and append zeroes in the end.
    # Testcase Runtime: 60ms
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def moveZeroes_1(self, nums):
        zeros = list()
        for i in range(len(nums)):
            if nums[i] is 0:
                zeros.append(i)
        
        for i in range(len(zeros)):
            if i+1 == len(zeros):
                prev, next = zeros[i], len(nums)
            else:
                prev, next = zeros[i], zeros[i+1]
            
            nums[prev-i:next-1-i] = nums[prev+1:next]
        
        nums[:-len(zeros)-1:-1] = [0]*len(zeros)
    
    # Solution 2: Swap the positions of newly found non-zero element and the first zero element next to the last found non-zero element in the list.
    # Testcase Runtime: 79ms
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def moveZeroes_2(self, nums):
        fast, slow = 0, 0
        while fast < len(nums):
            if nums[fast] == 0:
                fast+=1
            elif fast != slow:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                fast+=1
                slow+=1
            else:
                fast+=1
                slow+=1