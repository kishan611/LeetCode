class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res=""
        j=0
        for i in spaces:
            while j<i:
                res+=s[j]
                j+=1
            res+=" "
        res+=s[j:]
        return res