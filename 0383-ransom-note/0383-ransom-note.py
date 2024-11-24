from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_map = defaultdict(int)
        for letter in magazine:
            hash_map[letter] += 1

        for letter in ransomNote:
            if hash_map[letter] == 0:
                return False
            else:
                hash_map[letter] -= 1
        return True