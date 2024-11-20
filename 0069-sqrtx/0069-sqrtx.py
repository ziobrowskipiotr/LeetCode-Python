class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left = int(math.e ** (0.5*math.log(x, math.e)))
        right = left + 1
        print(left)
        return left if right*right > x else right