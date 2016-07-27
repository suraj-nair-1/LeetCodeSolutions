class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def searchdown(dc, num):
            total = 0
            n = num
            while dc.has_key(n):
                total += dc[n]
                n -= 1
            dc[num] = total
            for i in range(n+1, num):
                dc.pop(i, None)
            
        def searchup(dc, num):
            total = 0
            n = num
            while dc.has_key(n):
                total += dc[n]
                n += 1
            for i in range(num, n):
                dc.pop(i, None)
            return total
            
        dc = {}
        for item in nums:
            dc[item] = 1
        print dc
        
        mx = 0
        while len(dc) > 0:
            num = dc.keys()[0]
            searchdown(dc, num)
            size = searchup(dc, num)
            mx = max(mx, size)
        return mx
            
        
        
        # while len(dc.keys()) > 0:
        #     next_key = dc.keys(0)
        #     while dc.has_key(next_key):
                