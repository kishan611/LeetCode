class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m=len(land)
        n=len(land[0])
        res=[]
        def dfs(i,j,rmax,cmax):
            if i<0 or i>=m or j<0 or j>=n or land[i][j]==0:
                return rmax,cmax
            land[i][j]=0
            rmax=max(rmax,i)
            cmax=max(cmax,j)
            rmax,cmax=dfs(i,j+1,rmax,cmax)
            rmax,cmax=dfs(i+1,j,rmax,cmax)
            return rmax,cmax
        for i in range(m):
            for j in range(n):
                if land[i][j]==1:
                    rmax,cmax=dfs(i,j,-1,-1)
                    res.append([i,j,rmax,cmax])
        return res
                        
                
                
                    
        