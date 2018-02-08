# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        
        queue = list()
        queue.append(root)
        tree2array = list()

        while len(queue) > 0:
            current = queue.pop(0)
            if current is None:
                tree2array.append(None)
                continue
            tree2array.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        
        i = 1
        while 2**(i+1)-1 < len(tree2array):
            m, n = 2**i-1, 2**(i+1)-1
            sub = tree2array[m:n]
            rev_sub = tree2array[m:n]
            rev_sub.reverse()
            if sub != rev_sub:
                return False
            i += 1
        return True