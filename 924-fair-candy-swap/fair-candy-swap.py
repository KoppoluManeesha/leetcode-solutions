class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        sumA=sum(aliceSizes)
        sumB=sum(bobSizes)
        diff=(sumA-sumB)//2
        bobSet=set(bobSizes)
        for x in aliceSizes:
            y = x-diff
            if y in bobSet:
                return [x,y]