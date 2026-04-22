class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       count = 0
       con =0

       for i in range(len(nums)):
         if count == 0:
            con = nums[i]
            count = 1 

         elif con == nums[i]:
            count +=1
         else:
            count -=1
       return con