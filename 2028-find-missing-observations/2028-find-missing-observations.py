class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m=len(rolls)
        nsum=(m+n)*mean-sum(rolls)
        if nsum<n or nsum>n*6:
            return []
        q,r=nsum//n,nsum%n
        return [q+(1 if i<r else 0) for i in range(n)]


        