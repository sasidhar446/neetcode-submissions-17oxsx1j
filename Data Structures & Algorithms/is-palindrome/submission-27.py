class Solution:

    def isValid(self, s: str) -> bool:
        return (ord('a') <= ord(s) <= ord('z') or
                ord('A') <= ord(s) <= ord('Z') or
                ord('0') <= ord(s) <= ord('9'))

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


