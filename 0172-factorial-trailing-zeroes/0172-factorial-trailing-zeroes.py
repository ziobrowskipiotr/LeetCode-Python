class Solution:
    def trailingZeroes(self, n: int) -> int:
        num_zer = 0
        for i in range(5, n+1, 5):
            while i % 5 == 0:
                i /= 5
                num_zer += 1
        return num_zer