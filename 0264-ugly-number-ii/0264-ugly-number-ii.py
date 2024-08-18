from heapq import heappop,heappush 
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        visited={1}
        uglynums=[1]
        allowedp=[2,3,5]
        res=1
        for _ in range(n):
            res=heappop(uglynums)
            for i in allowedp:
                num=i*res
                if num not in visited:
                    heappush(uglynums,num)
                    visited.add(num)
        return res
            
        
        