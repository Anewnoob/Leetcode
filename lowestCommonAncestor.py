#面试题68 - II. 二叉树的最近公共祖先
#给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q: return root
        #递归找p,q
        left = self.lowestCommonAncestor(root.left, p, q)           #left,right三种可能值。null q,p
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left and not right: return 
        if not left: return right
        if not right: return left
        return root
