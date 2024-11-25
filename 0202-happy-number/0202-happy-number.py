class Solution:
    def isHappy(self, n: int) -> bool:
        set_n = set()
        while n != 1:
            if n in set_n:
                return False
            else:
                set_n.add(n)
            temp, n = n, 0
            while temp > 0:
                n += (temp%10)**2
                temp //= 10
        return True
        