"""
Topic:
    Given a binary tree, return all duplicate subtrees.
    Two trees are duplicate if they have the same structure with same node values.
    For each kind of duplicate subtrees, you only need to return the root node of any one of them.
"""

import collections
class Solution:

    """
    :type root: TreeNode
    :rtype: List[TreeNode]
    """

    # Solution 1: Convert the tree structure into a string which uses '#' to represent null.
    #             Use a counter to record all the subtree structure and append the node when the same string appears
    # Time Complexity: O(N) due to the tree traversal of all nodes. [The time for creating the string is neglected]
    # Space Complexity: O(N) due to the recursion of dfs takes O(logN) and the size of the counter takes O(N) [the size of key in the counter is neglected]
    # Testcase Runtime: 84ms
    def findDuplicateSubtrees_1(self, root):

        collection = collections.Counter()
        ans = []

        def dfs(node):
            if not node:
                return '#'

            rep = str(node.val) + dfs(node.left) + dfs(node.right)
            collection[rep] += 1
            if collection[rep] == 2:
                ans.append(node)
            return rep

        dfs(root)
        return ans

    # Solution 2: Assign the tree structure to a unique ID, say the length of the dictionary at the moment.
    #             Use a counter to store the IDs and append the node when the same ID appears.
    # Time Complexity: O(N) due to the tree traversal of all nodes.
    # Space Complexity: O(N) due to the recursion of dfs takes O(logN) and the size of the counter takes O(N)
    # Testcase Runtime: 100ms
    def findDuplicateSubtrees_2(self, root):
        d = collections.defaultdict()
        d.default_factory = d.__len__
        count = collections.Counter()
        result = []

        def dfs(node):
            if not node:
                return None
            key = (node.val, d[dfs(node.left)], d[dfs(node.right)])
            count[key] += 1
            if count[key] == 2:
                result.append(node)
            return key

        dfs(root)
        return result


