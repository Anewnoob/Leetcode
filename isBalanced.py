#面试题55 - II. 平衡二叉树
#输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(root):
            if not root: return 0
            left_depth = dfs(root.left)
            if left_depth < 0 : return -1
            right_depth = dfs(root.right)
            if right_depth < 0: return -1
            return max(left_depth,right_depth)+1 if abs(right_depth-left_depth) <= 1 else -1
        return dfs(root) != -1
