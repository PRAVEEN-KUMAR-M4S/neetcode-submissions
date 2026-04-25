class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            if i > 0 and nums[i - 1] == n:
                continue

            j, k = i + 1, len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    # skip duplicates for j
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    
                    # skip duplicates for k
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return res