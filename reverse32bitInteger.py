class Solution:
    def reverse(self, x: int) -> int:
        upperLimit = 2 ** 31 - 1 
        lowerLimit = -2 ** 31    
        reversedNumber = 0

        while x != 0:
            if reversedNumber > upperLimit / 10 or reversedNumber < lowerLimit / 10:
                return 0
            if x > 0:
                digit = x % 10 
            else:
                digit = x % -10
            reversedNumber = reversedNumber * 10 + digit
            x = math.trunc(x / 10)

        return reversedNumber
