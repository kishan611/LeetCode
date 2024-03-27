class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxl,left=0,0
        c={}
        for right,val in enumerate(s):
            c[val]=c.get(val,0)+1
            while c[val]>1:
                c[s[left]]-=1
                left+=1
            maxl=max(maxl,right-left+1)
        return maxl