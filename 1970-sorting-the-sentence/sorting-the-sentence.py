class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=list(s.split(" "))
        new_s=[""]*len(s)
        for word in s:
            pos = int(word[-1])-1
            new_s[pos] = word[:-1]
        return " ".join(new_s)