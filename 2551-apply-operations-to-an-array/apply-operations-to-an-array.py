class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
        non_zeros=[x for x in nums if x!=0]
        new_list=non_zeros+[0]*(len(nums)-len(non_zeros))
        return new_list
            