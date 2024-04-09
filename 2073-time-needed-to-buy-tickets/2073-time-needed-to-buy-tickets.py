class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n=len(tickets)
        count=0
        while tickets[k]>1:
            for i in range(n):
                if tickets[i]:
                    tickets[i]-=1
                    count+=1
        for i in range(k+1):
            if tickets[i]:
                count+=1
        return count