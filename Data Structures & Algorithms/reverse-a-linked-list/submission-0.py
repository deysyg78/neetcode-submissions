# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        #
        #none <-1   2->3->none
        # prev  curr
        while curr is not None:
            next_node = curr.next# 2
            curr.next = prev # 1->none
            #resetting
            prev = curr # 1
            curr = next_node
        return prev

