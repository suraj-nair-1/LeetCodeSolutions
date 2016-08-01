# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
            
        original = head
        count = 1
        
        last = None
        while count < m:
            last = head
            head = head.next
            count += 1
            
        if m == 1:
            end = head
        else:
            end = last
            
        last = head
        head = head.next
        count += 1
            
        while count <= n:
            temp = head.next
            head.next = last
            last = head
            head = temp
            count += 1
            
        if m == 1:
            end.next = head
            print "LIST:"
            og_end = last
            while last.next != None:
                print last.val
                last = last.next
            return og_end
        else:
            end.next.next = head
            end.next = last
            print "LIST:"
            end = original
            while end != None:
                print end.val
                end = end.next
            return original
            
            
            
            
            
        