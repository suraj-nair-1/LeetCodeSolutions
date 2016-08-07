class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # Finds left index if it exists
        low = -1
        high = len(nums)-1
        while low < high - 1:
            mid =  int(low + ((high - low) / 2))
            print mid
            if nums[mid] < target:
                low = mid
            elif nums[mid] >= target:
                high = mid
        print "____________________"
        left = low
        
        # Finds right index if it exists
        low = 0
        high = len(nums)
        while low < high - 1:
            mid =  int(low + ((high - low) / 2))
            print mid
            if nums[mid] <= target:
                low = mid
            elif nums[mid] > target:
                high = mid
        print "____________________"
        print high
        
        if nums[left + 1] != target or nums[high - 1] != target:
            return [-1,-1]
        else:
            return [left + 1, high - 1]
            