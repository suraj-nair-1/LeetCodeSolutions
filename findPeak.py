class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [-1*float("inf")] + nums + [-1*float("inf")]
        if len(nums) < 3:
            return 0
        
        left = 0
        right = len(nums) - 1
        while True:
            i = left + ((right - left) / 2)

            if nums[i-1] < nums[i] and nums[i+1] < nums[i]:
                return i-1
            elif nums[i-1] < nums[i] and nums[i+1] > nums[i]:
                left = i
            else:
                right = i
                