# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        if not root:
            return 0
        self.total = 0

        def dfs(node, currentSum):
            if not node:
                return 0

            currentSum += node.val

            if currentSum == targetSum:
                self.total += 1
            
            dfs(node.left, currentSum)
            dfs(node.right, currentSum)
        
        stack = [root]

        while stack:
            node = stack.pop()

            dfs(node, 0)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            
        return self.total
            
        