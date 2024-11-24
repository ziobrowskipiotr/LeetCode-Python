from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_s = defaultdict(int)
        for letter in s:
            map_s[letter] += 1
        for letter in t:
            if letter not in map_s:
                return False
            map_s[letter] -= 1
        for s_letter in s:
            if map_s[s_letter] > 0:
                return False
        return True