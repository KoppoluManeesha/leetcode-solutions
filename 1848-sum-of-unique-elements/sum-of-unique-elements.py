class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq={}
        sum_unique=0
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for val in freq:
            if freq[val]==1:
                sum_unique+=val
        return sum_unique
            

        