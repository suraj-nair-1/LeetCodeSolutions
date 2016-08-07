import math

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        high = num
        low = 0
        while low < high:
            mid = math.floor(low + (high - low) / 2)
            if mid == high or mid == low:
                return (mid ** 2 == num)
            print low, mid, high
            if mid**2 > num:
                high = mid
            elif mid**2 < num:
                low = mid
            else:
                return True
        return False
            
                
            