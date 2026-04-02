class Solution:
    def isalnum(self, c: str):
        return ord("a") <= ord(c) <= ord("z") or ord("A") <= ord(c) <= ord("Z") or ord("0") <= ord(c) <= ord("9")

    def isPalindrome(self, s: str) -> bool:
        curated_string = "".join([c.lower() for c in s if self.isalnum(c)])
        left, right = 0, len(curated_string) - 1
        while left <= right:
            if curated_string[left] != curated_string[right]:
                return False
            left += 1
            right -= 1
        return True

        

        