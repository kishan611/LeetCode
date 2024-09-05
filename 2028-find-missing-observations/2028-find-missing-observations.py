class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m=len(rolls)
        nsum=(m+n)*mean-sum(rolls)
        if nsum<n or nsum>n*6:
            return []
        res=[1]*n
        nsum-=n
        i=0
        while nsum>=5:
            res[i]+=5
            nsum-=5
            i+=1
        if nsum:
            res[i]+=nsum
        return res


        