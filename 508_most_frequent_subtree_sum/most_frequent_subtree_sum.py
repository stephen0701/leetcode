'''
Topic:
    Most Frequent Subtree Sum

Description:

Given the root of a tree, you are asked to find the most frequent subtree sum.
The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself).
Return all the values of subtree sum with the highest frequency in any order.

Example:
    Input 1 = [5, 2, -3], then return [2, -3, 4]
    (since all the values happen only once, return all of them in any order.)

    Input 2 = [5, 2, -5], then return [2]
    (since 2 happens twice, however -5 only occur once.)
'''

import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    def findFrequentTreeSum(self, root):

        if not root:
            return []

        sum_counter = collections.Counter()  # or collections.defaultdict(int)

        def subtree_sum(node):
            if node is None:
                return 0

            total = node.val + subtree_sum(node.left) + subtree_sum(node.right)
            sum_counter[total] += 1
            return total

        subtree_sum(root)

        max_count = max(sum_counter.values())
        return [k for k, v in sum_counter.items() if v == max_count]