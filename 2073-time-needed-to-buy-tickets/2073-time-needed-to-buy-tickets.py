class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n=len(tickets)
        nt=tickets[k]
        count=nt
        for i in tickets[:k]:
            if i<nt:
                count+=i
            else:
                count+=nt
        for i in tickets[k+1:]:
            if i<(nt-1):
                count+=i
            else:
                count+=nt-1
        return count