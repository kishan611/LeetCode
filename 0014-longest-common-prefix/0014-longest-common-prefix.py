class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        curr=strs[0]
        for i in strs[1::]:
            j=0
            while j<len(curr) and j<len(i) and curr[j]==i[j]:
                j+=1
            curr=curr[:j]
        return curr
        