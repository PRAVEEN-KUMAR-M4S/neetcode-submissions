class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}

        for s in strs:
            count=26*[0]

            for ch in s:
                index=ord(ch)-ord('a')
                count[index]+=1
            grouped_key=tuple(count)

            if grouped_key not in group:
                group[grouped_key] = []

            group[grouped_key].append(s)
        return list(group.values())
        