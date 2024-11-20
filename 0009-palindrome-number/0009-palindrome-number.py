class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x<10:
            return True
        temp_x = x
        len = 0
        while temp_x > 0:
            temp_x = int(temp_x/10)
            len += 1
        for i in range(int(len/2)):
            if (int(x/(10**(len-1-i))))%10 != int((x/(10**i)))%10:
                return False
        return True