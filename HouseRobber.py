dc = {}

def steal(nums):
    nms = str(nums)
    if dc.has_key(nms):
        return dc[nms]
    if len(nums) == 0:
        dc[nms] = 0
    elif len(nums) == 1:
        dc[nms] = nums[0]
    elif len(nums) == 2:
        dc[nms] = max(nums)
    else:
        dc[nms] = max(nums[0] + steal(nums[2:]), steal(nums[1:]))
    return dc[nms]
    
    

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return steal(nums)
        
        