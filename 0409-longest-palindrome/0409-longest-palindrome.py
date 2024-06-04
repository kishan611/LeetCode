from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        s=Counter(s)
        count,odd=0,0
        for i in s.values():
            if i%2==0:
                count+=i
            else:
                odd=1
                count+=i-1
        return count+odd
        