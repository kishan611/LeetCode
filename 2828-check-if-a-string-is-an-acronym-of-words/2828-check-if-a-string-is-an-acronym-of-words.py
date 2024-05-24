class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        n=len(words)
        m=len(s)
        if n!=m:
            return False
        for i in range(n):
            if s[i]!=words[i][0]:
                return False
        return True