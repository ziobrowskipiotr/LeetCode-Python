class Solution:
    def isPalindrome(self, x):
        if x<0:
            return False
        if x<10:
            return True
        if x%10 == 0:
            return False
        rev_number = 0
        while x > rev_number:
            rev_number = rev_number*10 + x%10
            x//=10
        return x == rev_number or x == rev_number//10