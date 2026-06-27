# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        merged = []
        if list1 >= list2:
            length = len(list1)
        else:
            length = len(list2)

        for i in range(length):
            if list1.val < list2.val:
                merged.append(list1)
                list1 = list1.next
            else:
                merged.append(list2
                list2 = list2.next
        
        return merged[0]
