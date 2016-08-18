# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        if head.next is None:
            return head
            
        # Identifies the numbers are duplicates
        cp = head
        s = set()
        while cp.next is not None:
            if cp.val == cp.next.val:
                s.add(cp.val)
            cp = cp.next
        
        # If all elements a duplicates
        while head.val in s:
            head = head.next
            if head is None:
                return head
            
        # If first element is duplicate
        c = head
        while c is not None:
            print c.val
            c = c.next
        
        # Removes elements that are duplicates
        og = head
        while head.next is not None:
            if head.next.val in s:
                head.next = head.next.next
            else:
                head = head.next
        
        return og
        