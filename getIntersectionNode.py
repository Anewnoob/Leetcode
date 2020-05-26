#输入两个链表，找出它们的第一个公共节点
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None: return
        p,q = headA,headB

        while p != q:
            p = p.next if p is not None else headB
            q = q.next if q is not None else headA
        return p
