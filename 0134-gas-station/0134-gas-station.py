class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        i=0
        curr,low=0,0
        for j,(g,c) in enumerate(zip(gas,cost)):
            if curr<low:
                i=j
                low=curr
            curr+=g-c
        if curr<0:
            return -1
        return i
        