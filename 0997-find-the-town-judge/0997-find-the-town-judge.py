class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a=set()
        for i in trust:
            a.add(i[0])
        x=n*(n+1)//2-sum(a)
        if x==0:
            return -1
        c=0
        for i in trust:
            if i[1]==x:
                c+=1
        if c==n-1:
            return x
        return -1