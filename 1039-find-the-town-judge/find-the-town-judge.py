class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        trust_a=[]
        trust_b=[]
        for a,b in trust:
            trust_a.append(a)
            trust_b.append(b)
        for i in range(1,n+1):
            if trust_b.count(i)==n-1 and i not in trust_a:
                return i
        return -1




                                                                                