class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        tot=0
        start=0
        for i,j in customers:
            if start<=i:
                start=i+j
                tot+=j
            else:
                start+=j
                tot+=(start-i)
        return tot/(len(customers))
            
            
        