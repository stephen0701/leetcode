class Solution:
    """
    :type nums: List[int]
    :rtype: int
    """
    # Solution: Use Dynamic Programming (Optimization)
    # Divide the problem into a sub-problem which is to find the maxSubArray that end with certain element
    # Update the global maximum value if a better result of the sub-problem is found
    def maxSubArray(self, nums):

        if not nums:
            return 0
        
        currentSum = maxSum = nums[0]
        for i in range(1, len(nums)):
            currentSum = max(nums[i], currentSum+nums[i])
            maxSum = max(maxSum, currentSum)
        return maxSum