# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        initial = ListNode(0)
        sol = initial
        carry_over = 0
        while (l1 is not None) or (l2 is not None):
            if l1 is None:
                l1_val = 0
            else:
                l1_val = l1.val
            if l2 is None:
                l2_val = 0
            else:
                l2_val = l2.val
            s = l1_val + l2_val + carry_over
            sol.val = s % 10
            carry_over = s / 10
            nxt = ListNode(0)
            sol.next = nxt
            last = sol
            sol = nxt
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry_over == 0:
            last.next = None
        else:
            sol.val = carry_over
        print initial
        return initial