class Solution:
    def trailingZeroes(self, n: int) -> int:
        def num_zeros(num):
            fives = 0
            while num % 5 == 0:
                num //= 5
                fives += 1
            return fives
        num_zer = 0
        for i in range(5, n+1, 5):
            num_zer += num_zeros(i)
        return num_zer
            
