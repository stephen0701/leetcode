/*
Topic:
    Remove Nth Node From End of List

Description:
    Given a linked list, remove the nth node from the end of list and return its head.

Note: 
    Given n will always be valid.
    Try to do this in one pass.
*/

class Solution {
    public:
    
        // Solution: Use a pointer ahead to find out the end of the Linked List, and the pointer to find the node previous to the target.
        //           Once the target is found, do the necessary removal operations.
        // Note: Adding a dummy node at the front helps solving the corner cases
        // Time Complexity: O(N)
        // Space Complexity: O(1)
        ListNode* removeNthFromEnd(ListNode* head, int n) {
            ListNode* dummy = new ListNode(0);
            dummy->next = head;
            
            ListNode* first = dummy;
            ListNode* second = dummy;
            for(int i=0; i<n+1;i++){
                first = first->next;
            }
            while(first){
                first = first->next;
                second = second->next;            
            }
            ListNode* removeNode = second->next;
            second->next = second->next->next;
            delete removeNode;
            return dummy->next;
        }
};