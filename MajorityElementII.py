class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums == []:
            return []
        diff1, diff2, candidate1, candidate2 = 0,0,0,1
        for n in nums:
            if diff1 == 0 and n != candidate2:
                candidate1 = n
                diff1 = 1
            elif diff2 == 0 and n != candidate1:
                candidate2 = n
                diff2 = 1
            elif n == candidate1:
                diff1 += 1
            elif n == candidate2:
                diff2 +=1 
            else:
                diff1 -= 1
                diff2 -= 1
        print candidate1, candidate2
        solution = []
        count1, count2 = 0, 0
        for n in nums:
            if n == candidate1:
                count1 += 1
            if n == candidate2:
                count2 += 1
        if count1 > len(nums) // 3:
            solution.append(candidate1)
        if (count2 > len(nums) // 3) and candidate2 != candidate1:
            solution.append(candidate2)
        return solution
            
        
        
