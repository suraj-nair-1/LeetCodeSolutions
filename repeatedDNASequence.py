class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        substrings = {}
        for i in range(0, len(s)-9):
            sub = s[i:i+10]
            if substrings.has_key(sub):
                substrings[sub] += 1
            else:
                substrings[sub] = 1

        result = []
        for key in substrings.keys():
            if substrings[key] > 1:
                result.append(key)
        return result
        
        