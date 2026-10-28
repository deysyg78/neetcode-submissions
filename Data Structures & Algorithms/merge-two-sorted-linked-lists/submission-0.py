# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = list1
        new=[]
        while curr is not None:
            new.append(curr.val)
            curr=curr.next
        curr=list2
        while curr is not None:
            new.append(curr.val)
            curr=curr.next
        new.sort()
        dummy=ListNode()
        tail=dummy

        for v in new:
            tail.next=ListNode(v)
            tail=tail.next
        return dummy.next

        
