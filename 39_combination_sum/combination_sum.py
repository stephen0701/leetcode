'''
Topic:
Combinations Sum

Description:
Given a set of candidate numbers (C) (without duplicates) and a target number (T),
Find all unique combinations in C where the candidate numbers sums to T.
The same repeated number may be chosen from C unlimited number of times.

Note:
    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

For example:
Given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[[2, 2, 3], [7]]

'''


class Solution:
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    # Solution 1: Dynamic Programming method, create a list that stores all possible combinations from 1 to target.
    #             The possible combinations should be result[target-n] + [n] (a number in candidates).
    #             Check that the numbers in result[target-n] should all be large than n to avoid duplicate combinations.
    def combinationSum_1(self, candidates, target):
        candidates.sort()
        result = [[]]
        for i in range(1, target + 1):
            combinations = list()
            if i in candidates:
                combinations.append([i])

            for n in candidates:
                if n > i:
                    break
                l = [[n] + x for x in result[i - n] if n <= x[0]]
                combinations.extend(l)
            result.append(combinations)
        return result[target]

    # Solution 2: Recursive method, recursively checking all the combinations of the numbers.
    #             If the candidate numbers are larger than the remainder, early return the loop.
    #             Find the candidate numbers in increasing order to avoid duplicate combinations.
    def combinationSum(self, candidates, target):
        result = []
        candidates.sort()
        self.recursive(candidates, [], result, 0, target)
        return result

    def recursive(self, candidates, combinations, result, index, target):
        if target == 0:
            result.append(combinations)
            return
        else:
            for i in range(index, len(candidates)):
                if candidates[i] > target:
                    break
                self.recursive(candidates, combinations + [candidates[i]], result, i, target - candidates[i])