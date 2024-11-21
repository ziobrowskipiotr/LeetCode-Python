class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        def dac(x: float, n: int) -> float:
            if n == 0:
                return 1
            elif n == 1:
                return x
            else:
                current_num = dac(x, n//2)
                if n%2 == 0:
                    return current_num * current_num
                else:
                    return x * current_num * current_num
        if n < 0:
            return 1/dac(x,abs(n))
        else:
            return dac(x,n)
