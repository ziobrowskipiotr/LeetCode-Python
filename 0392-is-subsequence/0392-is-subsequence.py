class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        ix1 = 0
        ix2 = 0
        while ix2 < len(t):
            if s[ix1] == t[ix2]:
                ix1 += 1
            if ix1 > len(s)-1:
                break
            ix2 += 1
        else:
            return False
        return True