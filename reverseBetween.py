# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if not (head and left < right):
            return head

        def helper(node, m):
            if m == left:
                prev = None
                current = node
                while m <= right:
                    current.next, prev, current = prev, current, current.next
                    m += 1
                node.next = current
                return prev
            elif m < left:
                node.next = helper(node.next, m + 1)
            return node

        return helper(head, 1)
        


        