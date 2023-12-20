class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1=101
        min2=101
        index=0
        for i in range(len(prices)):
            if prices[i]<min1:
                index=i
                min1=prices[i]
        for i in range(len(prices)):
            if i!=index and prices[i]<min2:
                min2=prices[i]
        if money-min1-min2>=0:
            return money-min1-min2
        return money