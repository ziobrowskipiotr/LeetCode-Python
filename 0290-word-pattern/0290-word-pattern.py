class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_pattern_s = {}
        map_s_pattern = {}
        list_word = s.split()
        if len(list_word) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in map_pattern_s and list_word[i] not in map_s_pattern:
                map_pattern_s[pattern[i]] = list_word[i]
                map_s_pattern[list_word[i]] = pattern[i]
            elif pattern[i] in map_pattern_s and map_pattern_s[pattern[i]] == list_word[i]:
                continue
            else:
                return False
        return True
