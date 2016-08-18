def ssets(nums):
    if nums == []:
        return [[]]
    subs = ssets(nums[1:])
    new = []
    for s in subs:
        n = s[:]
        n.append(nums[0])
        new.append(n)
    return subs + new

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return ssets(nums)
        