class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        res=[True]*n
        for i,j in edges:
            res[j]=False
        flag=0
        ans=-1
        for i in range(n):
            if res[i]:
                if flag:
                    return -1
                flag=1
                ans=i
        return ans