class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root==p or root==q:
            return root
        left_subtree=self.lowestCommonAncestor(root.left,p,q)
        right_subtree=self.lowestCommonAncestor(root.right,p,q)
        if left_subtree and right_subtree:
            return root
        elif left_subtree:
            return left_subtree
        else:
            return right_subtree
