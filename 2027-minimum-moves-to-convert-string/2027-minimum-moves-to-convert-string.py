class Solution:
    def minimumMoves(self, s: str) -> int:
        n=len(s)
        i=c=0
        while i<n:
            if s[i]=="O":
                i+=1
            else:
                i+=3
                c+=1
        return c
        