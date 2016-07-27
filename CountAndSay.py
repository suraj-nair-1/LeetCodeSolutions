class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def getNext(s):
            count = 1
            result = ""
            for i in range(0, len(s)-1):
                if s[i] == s[i+1]:
                    count += 1
                else:
                    result += (str(count) + s[i])
                    count = 1
            result += (str(count) + s[len(s)-1])
            return result
        i = 1
        current = "1"
        while i < n:
            print current
            current = getNext(current)
            i += 1
        print current
        return current
        