"""
Topic: 
    Add Two Numbers
Description:
    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order and each of their nodes contain a single digit.
    Add the two numbers and return it as a linked list.
Note:
    ．You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    # My Solution
    def addTwoNumbers(self, l1, l2):

        carry = 0
        head = None
        while l1 or l2:
            if l1 and l2:
                add = l1.val+l2.val+carry
                l1, l2 = l1.next, l2.next
            elif l1:
                add = l1.val+carry
                l1 = l1.next
            elif l2:
                add = l2.val+carry
                l2 = l2.next
            
            if not head:
                head = current = ListNode(add%10)
            else:
                current.next = ListNode(add%10)
                current = current.next
            carry = int(add/10)
            
        if carry == 1:
            current.next = ListNode(1)
            
        return head 

    # An Optimal and Elegant Solution
    def addTwoNumbers_2(self, l1, l2):
        carry = 0
        current = dummyHead = ListNode(0)
        while l1 or l2 or carry:
            value = carry
            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next
            
            carry, value = divmod(value, 10)
            current.next = ListNode(value)
            current = current.next
      
        return dummyHead.next