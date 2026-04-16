class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        count = Counter(digits)
        res = []
        for h in range(1,10):
            for t in range(10):
                for u in range(0,10,2):
                    needed = Counter([h,t,u])
                    possible = True
                    for digits,required_count in needed.items():
                        if count[digits]<required_count:
                            possible = False
                            break
                    if possible:
                        res.append(h*100+t*10+u)
        return res