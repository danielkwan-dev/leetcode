# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        prev = None
        curr = head

        while curr:
            next_n = curr.next
            curr.next    = prev
            prev = curr

            curr = next_n
        
        return prev
        