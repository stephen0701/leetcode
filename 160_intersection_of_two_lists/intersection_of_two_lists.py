"""
Topic: 
    Intersection of two linked lists
Description:
    Find the node at which the intersection of two singly linked lists begins.
Note:
    ．If the two linked lists have no intersection at all, return null.
    ．The linked lists must retain their original structure after the function returns.
    ．You may assume there are no cycles anywhere in the entire linked structure.
    ．Your code should preferably run in O(n) time and use only O(1) memory.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """
    :type headA, headB: ListNode
    :rtype: ListNode
    """
    # Solution 1: Traverse the first list and use a Hash Table to store the nodes of the list.
    #             Then, traverse the second list to check if there is a node same as one in the first list.
    #             Return the first node appeared.
    # Testcase Runtime: 367ms
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def getIntersectionNode_1(self, headA, headB):
    
        a = headA
        d = {}
        while a is not None:
            d[a] = True
            a = a.next
        
        b = headB
        while b is not None:
            if b in d:
                return b
            else:
                b = b.next
        return None
    
    # Solution 2: Create two pointers, each points to the head of the lists.
    #             Traverse its list until it reach the end of the list
    #             and assign the pointers to the head of the other list.
    #             If there is an intersection between two lists, the pointers will meet each other at the intersection.
    # Testcase Runtime: 383ms
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def getIntersectionNode(self, headA, headB):
        a, b = headA, headB
        while a != b:
            a = headB if a is None else a.next
            b = headA if b is None else b.next
        return a