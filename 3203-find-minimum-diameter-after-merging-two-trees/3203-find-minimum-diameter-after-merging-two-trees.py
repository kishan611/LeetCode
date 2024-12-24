class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def dia(edges):
            d={0:[]}
            for i,j in edges:
                if i not in d:
                    d[i]=[]
                if j not in d:
                    d[j]=[]
                d[i].append(j)
                d[j].append(i)
            ans=[0]
            def dfs(n,p):
                res=1
                for i in d[n]:
                    if i==p:
                        continue
                    dep=dfs(i,n)
                    ans[0]=max(ans[0],res+dep)
                    res=max(res,1+dep)
                return res
            dfs(0,-1)
            return ans[0]
        d1=dia(edges1)
        d2=dia(edges2)
        return max(d1-1,d2-1,d1//2+d2//2+1)