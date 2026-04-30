class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        currMin,currMax=1,1

        for n in nums:
            if n==0:
                currMin,currMax=1,1
                continue

            tempMin=currMin*n
            tempMax=currMax*n
            currMax=max(tempMin,tempMax,n)
            
            currMin=min(tempMin,tempMax,n)
            

            res=max(currMax,res)
        return res
        