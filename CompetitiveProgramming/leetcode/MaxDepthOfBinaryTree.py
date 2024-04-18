class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(node,depth):
            if not node: 
                return depth
            return max(dfs(node.left,depth+1),dfs(node.right,depth+1))
        return dfs(root,0)

