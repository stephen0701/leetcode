"""
Topic: 
    Min Stack
Description:
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Note:
    ．push(x) -- Push element x onto stack.
    ．pop() -- Removes the element on top of the stack.
    ．top() -- Get the top element.
    ．getMin() -- Retrieve the minimum element in the stack.
"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = list()
        
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.nums:
            self.nums.append((x,x))
        else:
            self.nums.append((x, min(x, self.nums[-1][1])))

    def pop(self):
        """
        :rtype: void
        """
        if self.nums:
            self.nums.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.nums[-1][0] if self.nums else None

    def getMin(self):
        """
        :rtype: int
        """
        return self.nums[-1][1] if self.nums else None