# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        stack = [root]
        solution = []
        while len(stack) > 0:
            root = stack.pop()
            solution.append(root.val)
            if not root.right == None:
                stack.append(root.right)
            if not root.left == None:
                stack.append(root.left)
        return solution
            
        