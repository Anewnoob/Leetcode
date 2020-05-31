#给定一个二叉树，检查它是否是镜像对称的。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        #dfs
        # def dfs(node1,node2):
        #     if node1 is None and node2 is None: return True
        #     if node1 is None or node2 is None: return False
        #     if node1.val != node2.val: return False
        #     return dfs(node1.left,node2.right) and dfs(node1.right,node2.left)

        # if root is None: return True
        # return dfs(root,root)

        #bfs
        queue = collections.deque()
        queue.append((root, root))
        while queue:
            left, right = queue.popleft()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
        return True


