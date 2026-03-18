class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        n=len(s)
        closest=[]
        for i in range(n):
            min_dist=float("inf")
            for j in range(n):
                if s[j]==c:
                    min_dist=min(min_dist,abs(i-j))
            closest.append(min_dist)
        return closest
                