class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        map_s_t = {}
        map_t_s = {}
        for i in range(len(s)):
            if s[i] not in map_s_t and t[i] not in map_t_s:
                map_s_t[s[i]] = t[i]
                map_t_s[t[i]] = s[i]
            elif s[i] in map_s_t and map_s_t[s[i]] == t[i]:
                continue
            else:
                return False
        print(map_s_t, map_t_s)
        return True