'''
Topic:
    Permutations

Description:
    Given a collection of distinct integers, return all possible permutations.
    
Example:
    Input: [1,2,3]
    Output:
    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]
'''

class Solution:
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # Solution 1: Iterative method, add the number if it doesn't exist in the permutations yet.
    # Time Complexity: sum(N!) where N = from 1 to len(nums) and extra time O(N) for searching through the permutations 
    # Space Complexity: O(1)
    def permute_1(self, nums):
        
        permutations = [[]]
        for i in range(len(nums)):
            permutations = [perm+[n] for perm in permutations for n in nums if n not in perm]
        return permutations
    
    # Solution 2: Iterative method, pick the numbers iteratively and insert it at all possbile occurence of current permutations.
    # Time Complexity: sum(N!) where N = from 1 to len(nums)
    # Space Complexity: O(1)
    def permute_2(self, nums):
        
        permutations = [[]]
        for n in nums:
            permutations = [perm[:i]+[n]+perm[i:] for perm in permutations for i in range(len(perm)+1)]
        return permutations
    
    # Solution 3: Recursive method, append a possible number at certain index iteratively, 
    #             and recursively use the same method to find the numbers of next index.
    # Time Complexity: O(N!)
    # Space Complexity: O(N)
    def permute_3(self, nums):

        result = []
        self.dfs(nums, [], result)
        return result
    
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            return
        
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)