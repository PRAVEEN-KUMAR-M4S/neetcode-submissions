class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        uniqueTriplets = set()

        for i in range(len(nums)):

            target=-nums[i]

            seen=set()

            for j in range(i+1, len(nums)):
                compl=target-nums[j]

                if compl in seen:
                    value = sorted([nums[i], nums[j], compl])
                    uniqueTriplets.add(tuple(value))
                seen.add(nums[j])
        return list(uniqueTriplets)
                

            







        
        