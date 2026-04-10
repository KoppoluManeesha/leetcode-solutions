class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """

        for i in range(left,right+1):
            found=False
            for start,end in ranges:
                if start <= i <= end:
                    found =True
                    break
            if not found:
                return False
        return True
        