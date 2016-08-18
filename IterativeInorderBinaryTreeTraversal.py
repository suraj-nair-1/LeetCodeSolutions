# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root is None:
            return []
        stack = [root]
        sol = []
        
        while len(stack) > 0:
            new_root = stack.pop()
            if (new_root.left is not None) or (new_root.right is not None):
                left = new_root.left
                right = new_root.right
                rt = TreeNode(new_root.val)
                if right is not None:
                    stack.append(right)
                stack.append(rt)
                if left is not None:
                    stack.append(left)
            else:
                sol.append(new_root.val)
        return sol
                    
                    
            