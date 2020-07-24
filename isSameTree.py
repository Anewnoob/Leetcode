给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # def dfs(p,q):
        #     if p is None and q is None: return True
        #     if p is None: return False
        #     if q is None: return False
        #     if p.val == q.val:
        #         return dfs(p.left,q.left) and dfs(p.right,q.right)
        #     else:
        #         return False
        # return dfs(p,q)  
        
        queue1 = collections.deque([q])
        queue2 = collections.deque([p])
        while queue1 and queue2:
            tmp1 = queue1.popleft()
            tmp2 = queue2.popleft()

            if tmp1 is None and tmp2 is None: continue
            if tmp1 is None: return False
            if tmp2 is None: return False   
            if tmp1.val == tmp2.val:
                queue1.append(tmp1.left)
                queue1.append(tmp1.right)
                queue2.append(tmp2.left)
                queue2.append(tmp2.right)
            else:
                return False
        if len(queue1) != len(queue2): return False
        return True
