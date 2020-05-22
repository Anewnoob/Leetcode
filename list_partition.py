#编写程序以 x 为基准分割链表，使得所有小于 x 的节点排在大于或等于 x 的节点之前。如果链表中包含 x，x 只需出现在小于 x 的元素之后(如下所示)。
#分割元素 x 只需处于“右半部分”即可，其不需要被置于左右两部分之间。
#示例:
#输入: head = 3->5->8->5->10->2->1, x = 5
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head: return
        i, j = head, head
        while i and j:
            if i.val < x:
                i = i.next
            else:
                if j == head:
                    if i.next:
                        j = i.next
                if j and j.val < x:
                    i.val, j.val = j.val, i.val
                    i = i.next
            j = j.next
        return head
