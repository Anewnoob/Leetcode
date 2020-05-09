#面试题34. 二叉树中和为某一值的路径
#输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res,path = [],[]
        def dfs(root,tar):
            if not root: return 
            path.append(root.val)
            tar -= root.val
            if tar == 0 and not root.left and not root.right:
                res.append(list(path))
            dfs(root.left,tar)
            dfs(root.right,tar)
            path.pop()
            
        dfs(root,sum)
        return res
