class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        new_list = defaultdict(list)

        for s in strs:
            sortedS = ''.join(sorted(s))
            new_list[sortedS].append(s)

        return list(new_list.values())
            