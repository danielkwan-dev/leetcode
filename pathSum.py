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
        :rtype: List[List[int]]
        """
        def dfs(root, targetSum, path):
            if not root:
                return None
            
            targetSum -= root.val
            path.append(root.val)
            if not root.left and not root.right :
                if targetSum == 0:
                    res.append(path[:])
            else:
                dfs(root.left, targetSum, path)
                dfs(root.right, targetSum, path)
            path.pop()
        
        res = []
        dfs(root, targetSum, [])
        return res
            
        