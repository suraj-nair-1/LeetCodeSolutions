class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums) - 2:
            if nums[i] == nums[i+1] and nums[i] == nums[i+2]:
                nums.pop(i);
            elif nums[i] == nums[i+1]:
                i += 2
            else:
                i += 1
        return len(nums)