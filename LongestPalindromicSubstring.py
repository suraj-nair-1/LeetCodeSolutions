def grow(s, i, j):
    while (i >= 0 and j < len(s)):
        if s[i] != s[j]:
            break
        i -= 1
        j += 1
    return s[i+1:j]
    
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
            
        mx = ""
        for i in range(0, len(s)):
            longest_odd = grow(s, i, i)
            longest_even = grow(s, i, i+1)
            if len(longest_odd) > len(mx):
                mx = longest_odd
            if len(longest_even) > len(mx):
                mx = longest_even
        return mx
            
            
        