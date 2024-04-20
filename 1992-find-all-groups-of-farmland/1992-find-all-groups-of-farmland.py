class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m=len(land)
        n=len(land[0])
        res=[]
        for i in range(m):
            for j in range(n):
                if land[i][j]==1:
                    x=i
                    while x<m and land[x][j]==1:
                        y=j
                        while y<n and land[x][y]==1:
                            land[x][y]=0
                            y+=1
                        x+=1   
                    res.append([i,j,x-1,y-1])
        return res
                        
                
                
                    
        