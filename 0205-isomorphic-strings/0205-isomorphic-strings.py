class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        hash_map = {}
        for i in range(len(s)):
            if s[i] in hash_map:
                if hash_map[s[i]] != t[i]:
                    return False
            elif t[i] in hash_map.values():
                return False
            hash_map[s[i]] = t[i]
        return True
