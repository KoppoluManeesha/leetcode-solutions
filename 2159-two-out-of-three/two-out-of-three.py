class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        s1=set(nums1)
        s2=set(nums2)
        s3=set(nums3)
        result=[]
        for num in s1|s2|s3:
            count=0
            if num in s1:
                count+=1
            if num in s2:
                count+=1
            if num in s3:
                count+=1
            if count>=2:
                result.append(num)
        return result
