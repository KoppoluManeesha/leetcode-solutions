class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        nums2=set(nums2)
        small=[]
        for num in nums1:
            if num in nums2:
                small.append(num)
        if small:
            return min(small)
        return -1
