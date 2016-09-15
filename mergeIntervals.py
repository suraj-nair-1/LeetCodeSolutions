# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals == []:
            return []
           
        # Find max value 
        mx = -1 * float("inf")
        for i in intervals:
             mx = max(max(i.start, i.end), mx)

        # Create array of that length. Array represents the whole span
        # of time which can be blocked into intervals
        res = [0] * (mx+1)
        
        
        for i in intervals:
            # If an interval is just one spot and is not part of any other 
            # interval, mark it with a 2
            if i.start == i.end:
                if res[i.end]==0:
                    res[i.end] = 2
            else:
                 # Mark the slot an interval fills with all 1s except for the last spot
                res[i.start:i.end] = [1] * (i.end - i.start)
                 # If the last spot is not part of an existing interval
                 # set it to -1
                if res[i.end]!=1:
                    res[i.end] = -1
            
        result = []    
        i = 0
        # iterates over time array. Saves continuous blocks of 1s as intervals
        # Saves 2s as a single interval block on their own
        while i < len(res):
            if res[i] == 1:
                start = i
                while res[i] == 1:
                    i += 1
                end = i - 1
                result.append(Interval(start, end+1))
            elif res[i] == 2:
                result.append(Interval(i, i))
            i += 1
        return result
                
            
        