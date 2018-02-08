"""
Topic: 
    House Robber
Description:
    Given a list of non-negative integers representing the amount of money of each house.
    Determine the maximum amount of money you can rob,
    but you can't take money from two adjcent houses.
"""

class Solution:
    """
    :type nums: List[int]
    :rtype: int
    """
    # Soultion 2: Use dynamic programming and a list to record the maximum profit in every cases.
    # Testcase Runtime: 74ms
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def rob_1(self, nums):
    
        if not nums:
            return 0
        max_money = list()
        for i in range(len(nums)):
            if i == 0:
                max_money.append(nums[i])
            elif i == 1:
                max_money.append(max(nums[0], nums[1]))
            else:
                max_money.append(max(nums[i]+max_money[i-2], max_money[i-1]))
        return max_money[-1]
    
    # Soultion 2: Use dynamic programming and without extra space
    # Testcase Runtime: 64ms
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def rob_2(self, nums):
    
        last, now = 0, 0
        for num in nums:
            last, now = now, max(last+num, now)
        return now