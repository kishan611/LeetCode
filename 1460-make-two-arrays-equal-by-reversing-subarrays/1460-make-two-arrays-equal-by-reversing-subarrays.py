class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        d={}
        for i in target:
            d[i]=d.get(i,0)+1
        for i in arr:
            if d.get(i,0)>0:
                d[i]-=1
            else:
                return False
        if any(d.values()):
            return False
        return True
        