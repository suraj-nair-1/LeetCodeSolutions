class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums = sorted(nums)
        
        sol = {}
        
        n = 0
        while n < len(nums)-2:
            i = n + 1
            j = len(nums) - 1
            s = -1 * nums[n]
            while i < j:
                # print n, i, j
                if (nums[i] + nums[j]) < s:
                    i += 1
                elif (nums[i] + nums[j]) > s:
                    j -= 1
                else:
                    sol[str([nums[n], nums[i], nums[j]])] = [nums[n], nums[i], nums[j]]
                    i += 1
            n += 1
        return sol.values()
                    
                    
            
        