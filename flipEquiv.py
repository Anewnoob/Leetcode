我们可以为二叉树 T 定义一个翻转操作，如下所示：选择任意节点，然后交换它的左子树和右子树。

只要经过一定次数的翻转操作后，能使 X 等于 Y，我们就称二叉树 X 翻转等价于二叉树 Y。

编写一个判断两个二叉树是否是翻转等价的函数。这些树由根节点 root1 和 root2 给出。


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(p,q):
            if p is None and q is None: return True
            if not p: return False
            if not q: return False
            if p.val != q.val: return False
            return (dfs(p.left,q.left) and dfs(p.right,q.right)) or (dfs(p.left,q.right) and dfs(p.right,q.left))
        return dfs(root1,root2)
