class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        freq_ch={}
        for ch in chars:
            freq_ch[ch]=freq_ch.get(ch,0)+1
        total_length=0
        for word in words:
            word_count={}
            is_good=True
            for ch in word:
                word_count[ch]=word_count.get(ch,0)+1
                if word_count[ch]>freq_ch.get(ch,0):
                    is_good=False
                    break
            if is_good:
                total_length+=len(word)
        return total_length


       