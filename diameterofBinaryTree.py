# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def diameter(node, result):
            if not node:
                return 0
            
            left = diameter(node.left, result)
            right = diameter(node.right, result)

            result[0] = max(result[0], left + right)

            return max(left, right) + 1
        
        result = [0]

        diameter(root, result)

        return result[0]

        
        