#请完成一个函数，输入一个二叉树，该函数输出它的镜像。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        # #dfs
        # if root is None: return None
        # root.left,root.right = self.mirrorTree(root.right),self.mirrorTree(root.left)
        # return root

        #bfd
        if root is None: return root
        stack = collections.deque([root])
        while stack:
            node = stack.popleft()
            if node.left is not None: stack.append(node.left)
            if node.right is not None: stack.append(node.right)
            node.left,node.right = node.right,node.left
        return root
