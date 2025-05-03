class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        res = float("inf")
        for i in [tops[0],bottoms[0]]:
            t = b = 0
            for j in range(n):
                if tops[j]==bottoms[j]==i:
                    continue
                if tops[j]==i:
                    t+=1
                elif bottoms[j]==i:
                    b+=1
                else:
                    break
            else:
                res = min(res,min(t,b))
        if res==float("inf"):
            return -1
        return res
            
            
        