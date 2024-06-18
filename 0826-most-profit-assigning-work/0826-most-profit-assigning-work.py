class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        profit=list(zip(profit,difficulty))
        profit.sort(reverse=True)
        worker.sort(reverse=True)
        res=0
        j=0
        n=len(worker)
        for i in profit:
            while j<n and i[1]<=worker[j]:
                res+=i[0]
                j+=1
            if j==n:
                break
        return res
        