class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        new_word1=""
        new_word2=""
        for word in word1:
            new_word1 += word
        for word_ in word2:
            new_word2 +=word_
        return new_word1==new_word2