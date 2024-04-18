class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, targetSum):
            if not node:
                return 0
            count=1 if node.val==targetSum else 0
            count+=dfs(node.left,targetSum-node.val)
            count+=dfs(node.right,targetSum-node.val)
            return count
        if not root:
            return 0
        return dfs(root,targetSum)+self.pathSum(root.left,targetSum)+self.pathSum(root.right,targetSum)
