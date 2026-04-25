class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group={}

        for n in nums:
            if n in group:
                group[n]+=1
            else:
                group[n]=1
        
        sorted_items=sorted(group.items(),key=lambda x:x[1],reverse=True)

        result=[]

        for key,value in sorted_items[:k]:
            result.append(key)
        return result
            
        
        