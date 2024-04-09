class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n=len(tickets)
        nt=tickets[k]
        count=nt*(k+1)+(n-k-1)*(nt-1)
        for i in tickets[:k]:
            if i<nt:
                count-=(nt-i)
        for i in tickets[k+1:]:
            if i<(nt-1):
                count-=(nt-1-i)
        return count