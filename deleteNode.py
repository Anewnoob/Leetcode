#给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。返回删除后的链表的头节点。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head is None: return
        if head.val == val:
            return head.next
        p,q = head,head.next
        while q is not None:
            if q.val == val:
                p.next = q.next
                return head
            p,q = p.next,q.next
        return head
