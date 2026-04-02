class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        # Dictionary to keep a count of all the unique characters in t.
        need = Counter(t)
        # Dictionary to keep a count of characters in the current window.
        have = {}
        
        # Number of unique characters in t that must be present in the window.
        required = len(need)
        # Number of unique characters in current window that meet the 'need' frequency.
        formed = 0
        
        # (window length, left, right)
        ans = float("inf"), None, None
        l, r = 0, 0

        while r < len(s):
            char = s[r]
            have[char] = have.get(char, 0) + 1

            # If the frequency of the current character matches its desired count in t
            if char in need and have[char] == need[char]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                char = s[l]

                # Save the smallest window found so far
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at 'l' is no longer part of the window
                have[char] -= 1
                if char in need and have[char] < need[char]:
                    formed -= 1

                l += 1    

            r += 1    
            
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]