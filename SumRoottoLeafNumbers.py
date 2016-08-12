# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None

def findNums(curr,  node, ls):
    if node is not None:
        print node.val
        curr = curr + str(node.val)
        if node.left is not None:
            findNums(curr, node.left, ls)
        if node.right is not None:
            findNums(curr, node.right, ls)
        if (node.right is None) and (node.left is None):
            ls.append(curr)
    
    

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ls = []
        findNums("", root, ls)
        s = 0
        print "____________"
        for l in ls:
            print l
            if l != '':
                s += int(l)
        return s
        