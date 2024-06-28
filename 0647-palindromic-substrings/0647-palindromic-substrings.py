class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        count=n
        for i in range(n):
            for j in range(i+2,n+1):
                x=s[i:j]
                if x==x[::-1]:
                    count+=1
        return count
                    