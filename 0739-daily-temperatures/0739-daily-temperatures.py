class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s=[]
        n=len(temperatures)
        count=0
        res=[0]*n
        for i in range(n-1,-1,-1):
            while count and temperatures[s[-1]]<=temperatures[i]:
                s.pop()
                count-=1
            if count:
                res[i]=s[-1]-i
            s.append(i)
            count+=1
        return res
                    
            
        