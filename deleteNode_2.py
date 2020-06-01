#给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。
#一般来说，删除节点可分为两个步骤：
#首先找到需要删除的节点；
#如果找到了，删除它。
#说明： 要求算法时间复杂度为 O(h)，h 为树的高度。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def dfs(root,key):
            if not root: return root
            if root.val == key:
                if root.left is None and root.right is None:
                    root = None
                elif root.right is not None:
                    # find the right
                    node = root.right
                    while node.left is not None:
                        node = node.left
                    root.val = node.val
                    root.right = dfs(root.right,root.val)
                else:
                    #find the left
                    node  = root.left
                    while node.right is not None:
                        node = node.right
                    root.val = node.val
                    root.left = dfs(root.left,root.val)
            elif root.val > key:
                root.left = dfs(root.left,key)
            else:
                root.right = dfs(root.right,key)
            return root

        return dfs(root,key) 
