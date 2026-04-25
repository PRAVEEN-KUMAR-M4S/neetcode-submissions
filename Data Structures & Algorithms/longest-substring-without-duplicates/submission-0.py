class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        checkSet=set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in checkSet:
                checkSet.remove(s[l])
                l+=1
            checkSet.add(s[r])
            res=max(res,r-l+1)
        return res




        