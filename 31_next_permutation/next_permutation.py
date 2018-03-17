'''
Topic:
    Next Permutation
    
Description:
    Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
    If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

For example:
    1,2,3 → 1,3,2
    3,2,1 → 1,2,3
    1,1,5 → 1,5,1
    
Note:
    The replacement must be in-place, do not allocate extra memory.
'''

class Solution:
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    # Solution: Loop the list from the right to find the first number that is descending.
    #           Swap it with the next larger number from its right.
    #           Rearrange the sub-list into ascending order.
    # Time Complexity: O(N)
    # Space Complexty: O(1)
    def nextPermutation(self, nums):
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                for j in range(len(nums)-1, i, -1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                nums[i+1:len(nums)] = nums[i+1:len(nums)][::-1]
                return
        nums[:] = nums[::-1]