class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m=len(mat)
        n=len(mat[0])
        count=0
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1 and mat[i].count(1)==1:
                    k=-1
                    while k<m-1:
                        k+=1
                        if k==i:
                            continue
                        if mat[k][j]==1:
                            break
                    else:
                        count+=1
        return count
                    
        