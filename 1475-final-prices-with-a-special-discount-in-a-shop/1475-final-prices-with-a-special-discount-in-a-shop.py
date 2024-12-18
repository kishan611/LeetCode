class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        s=[]
        n=len(prices)
        for i in range(n-1,-1,-1):
            while s and s[-1]>prices[i]:
                s.pop()
            x=prices[i]
            if s:
                prices[i]-=s[-1]
            s.append(x)
        return prices