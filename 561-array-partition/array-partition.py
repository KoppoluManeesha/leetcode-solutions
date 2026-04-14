class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        total_sum=0
        for i in range(0,len(nums),2):
            total_sum += nums[i]
        return total_sum
        