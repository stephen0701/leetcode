'''
Topic:
Longest Increasing Sub-sequence

Description:
Given an unsorted array of integers, find the length of longest increasing sub-sequence.

Note:
Your algorithm should run in at most O(N^2) time and space complexity.
It is possible to improve to O(NlogN) time complexity.

Example:
    Input: [10, 9, 2, 5, 3, 7, 101, 18]
    Output: 4, since the longest increasing subsequence is [2, 3, 7, 101], [2, 3, 7, 18], [2, 5, 7, 101] or [2, 5, 7, 18]
'''

import bisect
class Solution:
    """
    :type nums: List[int]
    :rtype: int
    """
    # Solution 1: Iterate the list to find each longest increasing sequence that ends with nums[i],
    #             and updates the longest results among these results.
    # Time Complexity: O(N^2)
    # Space Complexity: O(N)
    # Testcase Runtime: 1160ms
    def lengthofLIS_1(nums):

        results = []
        max_length = 0
        for i in range(len(nums)):
            ans = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    ans = max(ans, results[j] + 1)
            results.append(ans)
            max_length = max(ans, max_length)

        return max_length

    # Solution 2: Use a list to store the possible increasing sub-sequence.
    #             Iterate the list of numbers, binary search where the number should be inserted in the sequence list.
    #             Replace the element or append the element if the number is largest among the sequence list.
    #             Skip the above step if the element already appears in the sequence list.
    #             Note that the length of the sequence list will be the result in the end.
    #             However, the elements in the sequence list might not the correct longest increasing sub-sequence.
    #  Time Complexity: O(NlogN)
    # Space Complexity: O(N)
    # Testcase Runtime: 20ms
    def lengthOfLIS_2(self, nums):

        seq = []
        for n in nums:
            index = bisect.bisect(seq, n)
            if index != 0 and seq[index - 1] == n:
                continue
            if index == len(seq):
                seq.append(n)
            else:
                seq[index] = n

        return len(seq)
