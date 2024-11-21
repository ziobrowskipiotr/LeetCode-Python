class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left=0
        right=x
        while left<right:
            mid = (left+right)//2
            cur_pow = mid*mid
            if cur_pow < x:
                left = mid+1
            elif cur_pow > x:
                right = mid-1
            else:
                return mid
        return right