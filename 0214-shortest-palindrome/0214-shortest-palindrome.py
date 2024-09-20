class Solution:
    def shortestPalindrome(self, s: str) -> str:
        x=s[::-1]
        for i in range(len(x)+1):
            res=x[:i]+s
            if res==res[::-1]:
                return res
        