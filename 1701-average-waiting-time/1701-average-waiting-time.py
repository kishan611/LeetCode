class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        tot=customers[0][1]
        start=customers[0][0]+tot
        for i,j in customers[1::]:
            if start>i:
                tot+=start-i
                start+=j
            else:
                start=i+j
            tot+=j
        return tot/(len(customers))
            
            
        