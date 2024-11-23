class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        mask = 1
        count = 0
        for i in range(32):
            for num in nums:
                if (num & (mask<<i)) > 0:
                    count += 1
            if count % 3 > 0:
                result ^= mask<<i
            count = 0

        if result >= (1 << 31):
            result = result - (1 << 32)

        return result

