#面试题 04.12. 求和路径
#给定一棵二叉树，其中每个节点都含有一个整数数值(该值或正或负)。设计一个算法，打印节点数值总和等于某个给定值的所有路径的数量。注意，路径不一定非得从二叉树的根节点或叶节点开始或结束，但是其方向必须向下(只能从父节点指向子节点方向)。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def f(r, s):
            if r:
                s = [i + r.val for i in s] + [r.val]   #牛呀 s记录从根节点和中间节点到当前节点的和
                return s.count(sum) + f(r.left, s) + f(r.right, s)   #记录当前节点位置满足和的路径数量以及向下继续寻找满足的路径
            return 0
        return f(root, []) 
