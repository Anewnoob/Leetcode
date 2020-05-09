#面试题32 - III. 从上到下打印二叉树 III
#请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res,deque = [],collections.deque([root])
        while deque:
            tmp_deque = collections.deque()
            for _ in range(len(deque)):
                node = deque.popleft()
                if len(res)%2 == 0: tmp_deque.append(node.val)
                else: tmp_deque.appendleft(node.val)
                if node.left: deque.append(node.left)
                if node.right: deque.append(node.right)
            res.append(list(tmp_deque))
        return res
