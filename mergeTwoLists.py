# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        head = ListNode()
        curr = head
        
        if not l1 and not l2:
            return head.next
        if not l1:
            return l2
        if not l2:
            return l1
        
        while True:
            
            if l1.val <= l2.val:
                curr.next = l1
                curr = curr.next
                if l1.next == None:
                    curr.next = l2
                    break
                else:
                    l1 = l1.next
                    
            elif l1.val > l2.val:
                curr.next = l2
                curr = curr.next
                if l2.next == None:
                    curr.next = l1
                    break
                else:
                    l2 = l2.next
        
        return head.next

