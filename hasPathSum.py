#给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

#说明: 叶子节点是指没有子节点的节点。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        sum -= root.val
        if sum == 0 and not root.left and not root.right:
            return True
        left = self.hasPathSum(root.left,sum)
        right = self.hasPathSum(root.right,sum)
        return left or right
