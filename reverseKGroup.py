#给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
#k 是一个正整数，它的值小于或等于链表的长度。
#如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None: return
        i,len_list = head,0 
        while i:
            len_list += 1
            i = i.next
        if len_list < k: return head    

        q = head
        new_head = ListNode(-1)
        p = new_head
        tmp_list = []
        while len_list >= k:
            a = k
            #入栈
            while a > 0:
                tmp_list.append(q)
                q = q.next
                a -= 1
                len_list -= 1
            #出栈
            while tmp_list:
                p.next = tmp_list.pop()
                p = p.next
                p.next = None
        if len_list > 0:
            p.next = q
        return new_head.next

             

