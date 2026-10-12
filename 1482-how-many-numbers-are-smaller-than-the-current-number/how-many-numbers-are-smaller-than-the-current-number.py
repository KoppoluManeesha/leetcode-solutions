class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        num_count=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if nums[j] > nums[i]:
                    continue
                if nums[j] < nums[i]:
                    count+=1
            num_count.append(count)
        return num_count