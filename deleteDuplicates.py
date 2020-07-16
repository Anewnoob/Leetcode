#给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None: return head
        node=head
        while node and node.next:
            if node.val==node.next.val:
                node.next=node.next.next
            else:
                node=node.next
        return head
