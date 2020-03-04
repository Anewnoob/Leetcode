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