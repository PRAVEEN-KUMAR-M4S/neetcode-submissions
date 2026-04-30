class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxLeng=nums[0]
        currSum=0


        for n in nums:
            if currSum<0:
                currSum=0
            currSum+=n
            maxLeng=max(maxLeng,currSum)
        return maxLeng
        