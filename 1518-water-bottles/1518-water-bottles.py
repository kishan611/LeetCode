class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res=numBottles
        while numBottles>=numExchange:
            x=numBottles//numExchange
            res+=x
            numBottles=x+numBottles%numExchange
        return res
        