# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
#示例：
#输入：1->2->4, 1->3->4
#输出：1->1->2->3->4->4

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None: return l2
        if l2 is None: return l1
        p,q = l1,l2

        if p.val <= q.val:
            head = ListNode(p.val)
            p = p.next
        else:
            head = ListNode(q.val)
            q = q.next
        m = head
        while p is not None and q is not None:
            if p.val <= q.val:
                m.next = ListNode(p.val)
                m = m.next
                p = p.next
            else:
                node = ListNode(q.val)
                m.next = node
                m = m.next
                q = q.next
        while p is not None:
            m.next = ListNode(p.val)
            m = m.next
            p = p.next

        while q is not None:
            m.next = ListNode(q.val) 
            m = m.next
            q = q.next
        return head        
