class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res=""
        j=0
        for i in spaces:
            res+=s[j:i]
            res+=" "
            j=i
        res+=s[j:]
        return res