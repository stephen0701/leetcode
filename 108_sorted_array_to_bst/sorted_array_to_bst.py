"""
Topic:
    Sorted Array to Binary Search Tree
Description:
    Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
    A height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    :type nums: List[int]
    :rtype: TreeNode
    """

    # Solution: Use Divide and Conquer method to find the root element and recursively return the left and right node.
    # Time Complexity: O(logN)
    def sortedArrayToBST(self, nums):

        if len(nums) == 0:
            return None

        mid = int(len(nums) / 2)
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root