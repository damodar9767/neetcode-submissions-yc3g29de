class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        fre = {}

        for i in range(len(nums)):
            fre[nums[i]] = 1 + fre.get(nums[i],0)
            if fre[nums[i]] > len(nums)/2:
                return nums[i]
        return nums[0]