class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        strs.sort()
        curr=""
        i=0
        while i<len(strs[0]) and i<len(strs[-1]):
            if strs[0][i]==strs[-1][i]:
                curr+=strs[0][i]
            else:
                break
            i+=1
        return curr
        