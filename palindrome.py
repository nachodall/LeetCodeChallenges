class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        reversedNumber = 0
        originalNumber = x
        
        while x > 0:
            digit = x % 10
            reversedNumber = reversedNumber * 10 + digit
            x = x // 10

        return reversedNumber == originalNumber
