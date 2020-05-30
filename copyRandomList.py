#请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None: return head
        new_head = Node(-1,None,None)
        p,q = head,new_head
        visited = {}
        while p is not None:
            if p in visited:
                q.next = visited[p]
            else:
                new_node = Node(p.val,None,None)
                visited[p] = new_node
                q.next = new_node
            if p.random is not None:
                if p.random in visited:
                    q.next.random = visited[p.random]
                else:
                    new_node = Node(p.random.val,None,None)
                    visited[p.random] = new_node
                    q.next.random = new_node
            p = p.next
            q = q.next 
        return new_head.next

#         #DFS
#         def dfs(head):
#             if not head: return head
#             if head in visited:
#                 return visited[head]
#             node = Node(head.val,None,None)
#             visited[head] = node
#             node.next = dfs(head.next)
#             node.random = dfs(head.random)
#             return node
#         visited = {}
#         return dfs(head)
        
