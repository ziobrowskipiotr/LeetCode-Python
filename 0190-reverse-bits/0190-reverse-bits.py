class Solution:
    def reverseBits(self, n: int) -> int:
        mask_right = 1
        mask_left = 1 << 31
        for i in range(16):
            right = n & mask_right
            left = n & mask_left
            if right > 0:
                n |= mask_left
            else:
                n &= ~mask_left
            if left > 0:
                n |= mask_right
            else:
                n &= ~mask_right
            mask_right <<= 1
            mask_left >>= 1
        return n


        