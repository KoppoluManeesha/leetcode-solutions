class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        pairs={}
        for i in nums:
            pairs[i]=pairs.get(i,0)+1
        for count in pairs.values():
            if count%2!=0:
                return False
        return True



        