"""
Topic: 
    Maximum Depth of Binary Tree
Description:
    Given a binary tree, find its maximum depth.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
        :type root: TreeNode
        :rtype: int
    """
    
    # Solution 1: Depth First Search
    # Testcase Runtime: 74ms
    # Space Complexity: O(log n)
    def maxDepth_1(self, root):
    
        if root is None:
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
        
    # Solution 2: Breadth First Search, and use (current_node, depth) to record the current depth
    # Testcase Runtime: 90ms
    def maxDepth(self, root):
    
        depth = 0
        queue = list()
        queue.append((root, 1))
        while len(queue)>0:
            current = queue.pop(0)
            if current[0] == None:
                continue
                
            depth = current[1] if current[1] > depth else depth
            
            if current[0].left != None:
                queue.append((current[0].left, current[1]+1))
            if current[0].right != None:
                queue.append((current[0].right, current[1]+1))
        return depth
    
    # Solution 3: Breadth First Search, and use two loops to record the depth. The inner loop process all the nodes of same depth
    # Testcase Runtime: 86ms
    def maxDepth(self, root):
    
        if root == None:
            return 0
        
        depth = 0
        queue = list()
        queue.append(root)
        while len(queue)>0:
            depth += 1            
            n = len(queue)
            
            for i in range(n):
                node = queue.pop(0)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
        return depth