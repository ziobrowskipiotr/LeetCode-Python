from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_strs = defaultdict(list)
        for word in strs:
            map_strs[tuple(sorted(word))] += [word]
        return list(map_strs.values())