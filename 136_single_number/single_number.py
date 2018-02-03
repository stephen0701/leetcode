"""
Topic: 
    Single Number
Description:
    Given an array of integers, every element appears twice except for one. Find that single one.
Note:
    Your algorithm should have a linear runtime complexity. 
    It could be implemented without using extra memory.
"""

class Solution:
    """
    :type nums: List[int]
    :rtype: int
    """
    # Solution 1: Use a dictionary to record the element existed once, and remove it when it shows again.
    # Testcase Runtime: 76ms
    # Time Complexity: O(n)
    # Space Complexity: O(n), an extra dictionary is needed.
    def singleNumber_1(self, nums):

        if not nums:
            return 0
        
        unique = {}
        for num in nums:
            try:
                del unique[num]
                # unique.pop(num)
            except:
                unique[num] = True
        return unique.popitem()[0]
        
    # Solution 2: Mathematic operation
    # Testcase Runtime: 70ms
    # Time Complexity: O(n), summing up all the elements.
    # Space Complexity: O(n), an extra set is needed.
    def singleNumber_2(self, nums):
        return 2*sum(set(nums)) - sum(nums)
        
    # Solution 3: Bit manipulation, XOR of two same bits will return 0.
    # Testcase Runtime: 77ms
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def singleNumber_3(self, nums):
        unique = 0
        for num in nums:
            unique ^= num
        return unique
    
    # Solution 4: Similar method with #3. However, reduce() needs to be imported from the package "functools" first for Python3.
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def singleNumber_4(self, nums):
        return reduce(lambda x, y: x ^ y, nums)