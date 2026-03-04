class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        max_sum= 0 
        max_num=None
        for num in freq:
            if freq[num]>max_sum:
                max_sum=freq[num]
                max_num=num
        return max_num