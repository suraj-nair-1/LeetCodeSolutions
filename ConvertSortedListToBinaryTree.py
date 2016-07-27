# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def convert(listHead):
            if listHead == None:
                print "None"
                return listHead
            if listHead.next == None:
                print "Child is None", listHead.val
                return TreeNode(listHead.val)
            print listHead.val
            
            head = listHead
            length = 1
            while head.next != None:
                length += 1
                head = head.next
            mid = (length + (length % 2)) / 2
            
            
            
            length = 1
            head = listHead
            last = None
            while length < mid:
                length += 1
                last = head
                head = head.next
            print "MID", head.val
            left = None
            if last != None:
                print "BEFORE MID", last.val
                last.next = None
                left = convert(listHead)
            right = convert(head.next)
            root = TreeNode(head.val)
            root.left = left
            root.right = right
            return root
            
        return convert(head)
        
        
        
                
            
            
        