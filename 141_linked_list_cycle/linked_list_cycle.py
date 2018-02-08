"""
Topic: 
    Linked List Cycle
Description:
    Given a linked list, determine if it has a cycle in it.
Note:
    Could it be solved without extra space?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """
    :type head: ListNode
    :rtype: bool
    """
    # Solution 1: Use a dictionary to record the element shown before.
    # Testcase Runtime: 77ms
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def hasCycle_1(self, head):
        current = head
        m = {}
        while current is not None:
            if current in m:
                return True
            else:
                m[current] = True
                current = current.next
        return False
    
    # Solution 2: Use 2 pointers to determine whether the linked list is cyclic
    # Testcase Runtime: 65ms
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def hasCycle_2(self, head):
        fast, slow = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                return True
        return False