class Solution:
    def __init__(self):
        self.p=[]
        self.r=[]
        self.res=0
    def regionsBySlashes(self, grid: List[str]) -> int:
        n=len(grid)
        lines=n+1
        self.p=[i for i in range(lines*lines)]
        self.r=[1]*(lines*lines)
        for i in range(lines):
            for j in range(lines):
                if i==0 or j==0 or i==n or j==n:
                    c=i*lines+j
                    self.union(0,c)
        for i in range(n):
            for j in range(n):
                if grid[i][j]=='\\':
                    c1=i*lines+j
                    c2=(i+1)*lines+(j+1)
                    self.union(c1,c2)
                elif grid[i][j]=='/':
                    c1=(i+1)*lines+j
                    c2=i*lines+(j+1)
                    self.union(c1,c2)
        return self.res
    def union(self,i,j):
        pi=self.find(i)
        pj=self.find(j)
        if pi==pj:
            self.res+=1
        else:
            if self.r[pi]>self.r[pj]:
                self.p[pj]=pi
            elif self.r[pi]>self.r[pj]:
                self.p[pi]=pj
            else:
                self.p[pj]=pi
                self.r[pi]+=1
    def find(self,line):
        if self.p[line]==line:
            return line
        self.p[line]=self.find(self.p[line])
        return self.p[line]
        