#实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。
#注意：本题相对原题稍作改动
#示例：
#输入： 1->2->3->4->5 和 k = 2
#输出： 4

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        if head is None: return 
        pre_head = ListNode(None)
        pre_head.next = head
        p,q = pre_head,pre_head
        for _ in range(k):
            q = q.next
        while q.next is not None:
            q = q.next
            p = p.next
        return p.next.val
        
