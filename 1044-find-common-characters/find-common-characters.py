class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        freq = [float('inf')] * 26
    
        for word in words:
            temp = [0] * 26
        
            for ch in word:
                temp[ord(ch) - ord('a')] += 1
        
            for i in range(26):
                freq[i] = min(freq[i], temp[i])
    
        result = []
    
        for i in range(26):
            result.extend([chr(i + ord('a'))] * freq[i])
    
        return result
        