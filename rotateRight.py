# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        
        length = 1
        dummy = head

        while dummy.next:
            dummy = dummy.next
            length += 1
        
        position = k % length
        if position == 0:
            return head
        
        current = head

        for _ in range(length - position - 1):
            current = current.next
        
        new_head = current.next
        current.next = None
        dummy.next = head

        return new_head

        
        