class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mine=arrays[0][0]
        maxe=arrays[0][-1]
        res=0
        for i in arrays[1::]:
            res=max(res,abs(i[-1]-mine),abs(maxe-i[0]))
            mine=min(mine,i[0])
            maxe=max(maxe,i[-1])
        return res
        