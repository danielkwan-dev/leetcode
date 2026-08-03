# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        if not root:
            return []
        
        queue = [root]
        result = []
        left_to_right = True

        while queue:
            currentLevel = []

            for i in range(len(queue)):
                node = queue.pop(0)
                currentLevel.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if not left_to_right:
                currentLevel.reverse()
                                      
            result.append(currentLevel)
            left_to_right = not left_to_right

    
        return result
        