class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        res=[-1]*n
        for i,j in edges:
            res[j]=i
        flag=0
        ans=-1
        for i in range(n):
            if res[i]==-1:
                if flag:
                    return -1
                flag=1
                ans=i
        return ans