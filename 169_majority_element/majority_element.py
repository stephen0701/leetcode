"""
Topic: 
    Single Number
Description:
    Given an array of size n, find the majority element. 
    The majority element is the element that appears more than floor(n/2) times.
Note:
    You may assume that the array is non-empty and the majority element always exist in the array.
"""
class Solution:
    """
    :type nums: List[int]
    :rtype: int
    """
    # Solution 1: Use Hash Map to record the amount of the numbers, and once the amount of a certain number is over n/2, 
    #             return it as the result.
    # Testcase Runtime: 94ms
    # Time Complexity: O(n)
    # Space Complexity: O(n)    
    def majorityElement_1(self, nums):
        count = {}
        half_size = int(len(nums)/2)
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
            
            if count[num] > half_size:
                return num
                
    # Solution 2: Sort the array and return the middle index of it since the answer will always occupy it.
    # Testcase Runtime: 84ms
    # Time Complexity: O(nlogn)
    # Space Complexity: O(1)
    def majorityElement_2(self, nums):
        nums.sort()
        return nums[len(nums)//2]
        
    # Solution 3: Boyer-Moore Voting Algorithm
    # Testcase Runtime: 86ms
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def majorityElement_3(self, nums):
        count = 0
        candidate = 0
        for num in nums:
            if count == 0:
                candidate = num
            
            if candidate == num:
                count += 1
            else:
                count -= 1
        return candidate