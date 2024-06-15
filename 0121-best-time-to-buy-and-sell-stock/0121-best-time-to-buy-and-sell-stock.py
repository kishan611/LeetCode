class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp=0
        mip=prices[0]
        for i in prices[1::]:
            mp=max(mp,i-mip)
            mip=min(mip,i)
        return mp
        