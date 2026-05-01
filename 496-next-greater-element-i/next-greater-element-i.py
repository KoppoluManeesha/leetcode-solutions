class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack=[]
        nextGreater ={}
        for num in nums2:
            while stack and num>stack[-1]:
                prev=stack.pop()
                nextGreater[prev] = num
            stack.append(num)
        while stack:
            nextGreater[stack.pop()]=-1
        return [nextGreater[num] for num in nums1]
            