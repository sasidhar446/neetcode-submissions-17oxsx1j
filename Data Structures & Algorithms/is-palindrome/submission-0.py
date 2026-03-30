class Solution:
    def isPalindrome(self, s: str) -> bool:
        curated_string = "".join([c.lower() for c in s if c.isalnum()])
        i, j = 0, len(curated_string) - 1
        print(curated_string)
        while i <= j:
            if curated_string[i] != curated_string[j]:
                return False
            i += 1
            j -= 1
        return True
        