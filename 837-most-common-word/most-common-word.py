class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        
        paragraph = paragraph.lower()
        
        cleaned = ""
        for ch in paragraph:
            if ch.isalpha():
                cleaned += ch
            else:
                cleaned += " "
        
        words = cleaned.split()
        
        banned = set(banned)
        freq = {}
        
        for word in words:
            if word not in banned:
                freq[word] = freq.get(word, 0) + 1
        
        max_word = ""
        max_count = 0
        
        for word in freq:
            if freq[word] > max_count:
                max_count = freq[word]
                max_word = word
        
        return max_word