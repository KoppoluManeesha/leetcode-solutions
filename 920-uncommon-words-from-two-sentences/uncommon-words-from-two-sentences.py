class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        new_s1=list(s1.split(" "))
        new_s2=list(s2.split(" "))
        result=[]
        both=new_s1+new_s2
        for word in both:
            if word in new_s1 and word not in new_s2 and new_s1.count(word)==1:
                result.append(word)
            elif word in new_s2 and word not in new_s1 and new_s2.count(word)==1:
                result.append(word)
        return result