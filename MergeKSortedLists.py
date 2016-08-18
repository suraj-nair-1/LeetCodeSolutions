# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for head in lists:
            if head is not None:
                heapq.heappush(heap, (head.val, head.next))
        if heap == []:
            return None
        
        val, nxt = heapq.heappop(heap)
        if nxt is not None:
            heapq.heappush(heap, (nxt.val, nxt.next))
            
        head = ListNode(val)
        res = head
        while heap:
            val, nxt = heapq.heappop(heap)
            if nxt is not None:
                heapq.heappush(heap, (nxt.val, nxt.next))
            n = ListNode(val)
            res.next = n
            res = n
        return head
            