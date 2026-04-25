class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group={}

        for num in nums:
            group[num]=group.get(num,0)+1
        
        # bucket

        bucket=[[] for _ in range(len(nums)+1)]

        # adding to bucket

        for num,count in group.items():
            bucket[count].append(num)
        
        # taking top k element

        result=[]

        for i in range(len(bucket)-1,0,-1):
            for n in bucket[i]:
                result.append(n)
            if(len(result)==k):
                return result



        