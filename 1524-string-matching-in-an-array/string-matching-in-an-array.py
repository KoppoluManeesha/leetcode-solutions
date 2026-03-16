class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        sub_str=[]
        n=len(words)
        for i in range(n):
            for j in range(n):
                if i != j and words[i] in words[j]:
                    sub_str.append(words[i])
                    break
        return sub_str
