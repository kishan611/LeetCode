class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        d=e=0
        while numBottles:
            d+=1
            e+=1
            numBottles-=1
            if e==numExchange:
                e=0
                numBottles+=1
        return d
                
        