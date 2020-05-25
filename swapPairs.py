# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or not head.next: return head
        h = ListNode(None)
        h.next = head
        c = h 
        while c.next and c.next.next:
            a,b = c.next,c.next.next
            #swap
            c.next,a.next = b,b.next
            b.next = a 

            #init
            c = c.next.next
        return h.next
