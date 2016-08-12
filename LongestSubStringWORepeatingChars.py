class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)
        i = 0
        j = 1
        counts = {}
        counts[s[i]] = 1
        last_is_good = True
        mx = 1, ""
        while True:
            if last_is_good and j < len(s):
                j += 1
                if counts.has_key(s[j-1]):
                    # If adding j-1th element keeps the substring distinct
                    if counts[s[j-1]] == 0:
                        if len(s[i:j]) > mx[0]:
                            mx = len(s[i:j]), s[i:j]
                        counts[s[j-1]] = 1
                    # If adding j-1th element causes a duplicate character
                    else:
                        last_is_good = False
                        counts[s[j-1]] += 1
                # If adding j-1th element keeps the substring distinct
                else:
                    if len(s[i:j]) > mx[0]:
                        mx = len(s[i:j]), s[i:j]
                    counts[s[j-1]] = 1
            else:
                while s[i] != s[j-1]:
                    counts[s[i]] -= 1
                    i += 1
                counts[s[i]] -= 1
                i += 1
                last_is_good = True
            # print counts
            # print i, j, last_is_good
            if j == len(s) and last_is_good:
                break
                
        # print mx
        return mx[0]
                
                
            
                