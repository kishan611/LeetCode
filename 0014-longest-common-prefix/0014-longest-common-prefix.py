class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        curr=strs[0]
        for i in strs[1::]:
            j=0
            while j<(min(len(curr),len(i))):
                if curr[j]!=i[j]:
                    break
                j+=1
            curr=curr[:j]
        return curr
        