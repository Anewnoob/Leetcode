#面试题54. 二叉搜索树的第k大节点
#给定一棵二叉搜索树，请找出其中第k大的节点。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.k  = k
        def dfs(root):
            if not root: return 
            dfs(root.right)
            if self.k == 0: return 
            self.k -= 1
            if self.k == 0: self.res = root.val
            dfs(root.left)
        dfs(root)
        return self.res
        
