#面试题32 - II. 从上到下打印二叉树 II
#从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, deque = [],collections.deque([root])
        while deque:
            tmp_deque = collections.deque()
            for _ in range(len(deque)):
                node = deque.popleft()
                tmp_deque.append(node.val)
                if node.left: deque.append(node.left)
                if node.right: deque.append(node.right)
            res.append(list(tmp_deque))
        return res
