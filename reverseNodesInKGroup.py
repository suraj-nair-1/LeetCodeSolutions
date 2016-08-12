# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def reverseK(head, last, k):
    # Checks if the current segment is of length
    # longer than k. If it is, then returns the current segment 
    # unchanged
    j = 0
    cp = head
    while j < k and (cp is not None):
        cp = cp.next
        j += 1
    if j < k:
        return head, None, None
        
    # Reverses a segment of length k given 
    # the head
    i = 0
    og  = head
    while (head is not None) and i < k:
        nxt = head.next
        head.next = last
        last = head
        head = nxt
        i += 1
    og.next = head
    return last, head, og

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # Reverse the first segment of length k
        last = None
        res, head, last = reverseK(head, last, k)
        original = res
        # Saves the head of the list, and reverses
        # the rest
        while head is not None:
            prev = last
            res, head, last = reverseK(head, last, k)
            if res is not None:
                prev.next = res
        return original

        