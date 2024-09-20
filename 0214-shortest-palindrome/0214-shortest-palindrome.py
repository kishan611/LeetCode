class Solution:
    def shortestPalindrome(self, s: str) -> str:
        res = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(res[i:]):
                return res[:i] + s