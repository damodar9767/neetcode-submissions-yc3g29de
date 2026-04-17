class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0 
        con = None

        for num in nums:
            if count == 0:
                count = 1
                con = num

            elif num == con:
                count +=1
            else:
                count -=1

        return con