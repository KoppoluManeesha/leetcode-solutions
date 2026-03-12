class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_value=max(nums)
        index=nums.index(max_value)
        for n in nums:
            if n != max_value and max_value < n*2:
                return -1
        return index
