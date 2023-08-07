class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        vistos = set() #se usa un set porque no contiene repetidos, y la operacion pertenece corre en O(1)
        l_pointer = 0
        r_pointer = 0
        maxi = 0
        
        for r_pointer in range (len(s)):
            while s[r_pointer] in vistos:
                vistos.remove(s[l_pointer])
                l_pointer += 1
            vistos.add(s[r_pointer])
            maxi = max(maxi,len(vistos))

        return maxi
