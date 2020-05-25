# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # #优先队列  more better
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    #     if not lists: return
    #     K = len(lists)
    #     if K == 1: return lists[0]
    #     val_list = []

    #     import heapq
    #     for l in lists:
    #         while l:
    #             heapq.heappush(val_list,l.val) 
    #             l = l.next
    #     head = ListNode(None)
    #     cur = head 

    #     while val_list:
    #         node = ListNode(heappop(val_list))
    #         cur.next = node 
    #         cur = cur.next
    #     return head.next

    #分治法
    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(None)
        cur = head 
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                cur.next = ListNode(l1.val)
                l1 = l1.next
            else:
                cur.next = ListNode(l2.val)
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l2 is None else l2
        return head.next


    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return
        K = len(lists)
        if K == 1: return lists[0]
        mid = K // 2
        return self.merge(self.mergeKLists(lists[:mid]),self.mergeKLists(lists[mid:]))
