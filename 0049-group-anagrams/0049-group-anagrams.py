from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_strs = defaultdict(list)
        result = []
        for word in strs:
            temp = str(sorted(word))
            map_strs[temp] += [word]
        return list(map_strs.values())