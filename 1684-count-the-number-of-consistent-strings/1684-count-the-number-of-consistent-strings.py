class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res=0
        for i in words:
            if all(j in allowed for j in i):
                res+=1
        return res