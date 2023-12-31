class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        count=-1
        fc={}
        for i in range(len(s)):
            if s[i] in fc:
                count=max(count,i-fc[s[i]]-1)
            else:
                fc[s[i]]=i
        return count
        
        