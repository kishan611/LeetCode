class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def helper(n,quantities,item):
            if item==0:
                return False
            s=0
            for p in quantities:
                s+= (p-1) // item + 1
                if s > n:
                    return False
            return True
        l,h=1,max(quantities)
        res=-1
        while l<=h:
            mid=(l+h)//2
            if helper(n,quantities,mid):
                res= mid
                h=mid-1
            else:
                l=mid+1
        return res
            