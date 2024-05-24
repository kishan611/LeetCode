class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        x="".join([x[0] for x in words])
        return x==s