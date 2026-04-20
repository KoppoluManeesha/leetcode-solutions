class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        for ch in range(len(s)-1):
            count+=abs(ord(s[ch])-ord(s[ch+1]))
        return count
