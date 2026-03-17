class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
       
        i=0
        for word in words:
            for ch in word:
                if i >= len(s) or s[i] != ch:
                    return False
                i += 1
            
            if i == len(s):
                return True
        
        return False