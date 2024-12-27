class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res=0
        val=values[0]
        for i in values[1:]:
            res=max(res,i+val-1)
            val=max(val-1,i)
        return res