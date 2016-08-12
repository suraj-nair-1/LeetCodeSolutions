class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        twos, threes, fives = [1], [1], [1]
        ugly = 0
        two_count, three_count, five_count = 0,0,0
        
        for i in range(0, n):
            ugly = min(twos[two_count], threes[three_count], fives[five_count])
            if ugly == twos[two_count]:
                two_count += 1
            if ugly == threes[three_count]:
                three_count += 1
            if ugly == fives[five_count]:
                five_count += 1
            twos.append(ugly * 2)
            threes.append(ugly * 3)
            fives.append(ugly * 5)
        return ugly
            