class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        for i in range(n-1,-1,-1):
            for j in range(i):
                if nums[j]%2 != 0:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        return nums