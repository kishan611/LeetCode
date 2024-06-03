class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i=0
        j=0
        maxl=0
        while j<len(s) and i<len(t):
            if s[j]==t[i]:
                i+=1
            j+=1
        return len(t)-i