class Solution:

    def isValid(self, c: str):
        return (ord('A') <= ord(c) <= ord('Z') or 
               ord('a') <= ord(c) <= ord('z') or 
               ord ('0') <= ord(c) <= ord('9'))

    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while not self.isValid(s[left]) and left < right:
                left += 1
            while not self.isValid(s[right]) and left < right:
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -=1
        return True

        


