"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        newNode=ListNode(0)
        sumNode=newNode
        carry=0
        while l1.val>=0 or l2.val>=0:
            x=l1.val if l1.val>=0 else 0
            y=l2.val if l2.val>=0 else 0
            sum=x+y+carry
            carry=sum//10
            newNode.val=sum%10
            l1=l1.next if l1.next else ListNode(-1)
            l2=l2.next if l2.next else ListNode(-1)
            if l1.val>=0 or l2.val>=0 or carry:
                newNode.next=ListNode(0)
                newNode=newNode.next
        if carry==1:
            newNode.val=1
        return sumNode