class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i=0
        n=len(t)
        for j in s:
            if i<n and j==t[i]:
                i+=1
        return n-i