class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x=len(word1)
        y=len(word2)
        i=0
        s=""
        while i<x and i<y:
            s+=word1[i]+word2[i]
            i+=1
        if i<x:
            s+=word1[i:]
        if i<y:
            s+=word2[i:]
        return s