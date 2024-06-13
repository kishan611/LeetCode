class Solution:
    def countOdds(self, low: int, high: int) -> int:
        l=low%2
        h=high%2
        if l and h:
            return (high-low)//2+1
        return  (high-low)//2+l+h
        