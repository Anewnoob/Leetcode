# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        #double pointer--
        # if head is None: return

        # length = 0
        # t = head
        # while t is not None:
        #     t = t.next
        #     length += 1
        # if n == length:
        #     head = head.next
        #     return head
        # p,q = head,head
        # for _ in range(n):
        #     p = p.next
        # while p.next is not None:
        #     p = p.next
        #     q = q.next
        # q.next = q.next.next
        # return head

        #double pointer--
        Node = ListNode(None)
        Node.next = head
        first,slow = Node,Node
        for i in range(n):
            first = first.next
        while first.next != None:
            first = first.next
            slow = slow.next
        slow.next = slow.next.next
        return Node.next
