# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if not root:
            return 0 
    
        queue = [root]
        depth = 0

        while queue:
            currentLevel = []
            depth += 1

            for i in range(len(queue)):
                node = queue.pop(0)

                currentLevel.append(node.val)

                if not node.left and not node.right:
                    return depth

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                                            

        