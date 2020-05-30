#定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # #超出时间限制 用栈的思想
        # if head is None: return head
        # node_stack = list()
        # #入栈
        # while head is not None:
        #     node_stack.append(head)
        #     head = head.next
        # #出栈
        # new_head = ListNode(-1)
        # cur = new_head
        # while node_stack:
        #     cur.next = node_stack.pop()
        #     cur = cur.next
        # return new_head.next

        #双指针
        if head is None: return None
        p = head
        q = None
        while p is not None:
            node = ListNode(p.val)
            node.next = q
            q = node
            p = p.next
        return q


