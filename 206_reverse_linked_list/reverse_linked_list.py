'''
Topic:
Reverse Linked List

Description:
Reverse a singly linked list.

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    :type head: ListNode
    :rtype: ListNode
    """

    # Solution 1: Iterative method
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def reverseList_1(self, head):

        prev, current = None, head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev

    # Solution 2: Recursive method
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    def reverseList_2(self, head):

        if not head or not head.next:
            return head

        current = head
        head = self.reverseList(current.next)
        current.next.next = current
        current.next = None
        return head