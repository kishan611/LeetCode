from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ct=Counter(t)
        ms=""
        ml=float('inf')
        i=0
        for j in range(len(s)):
            if s[j] in ct:
                ct[s[j]]-=1
            while all(val<=0 for val in ct.values()):
                if j-i+1<ml:
                    ml=j-i+1
                    ms=s[i:j+1]
                if s[i] in ct:
                    ct[s[i]]+=1
                i+=1
        return ms
            
        