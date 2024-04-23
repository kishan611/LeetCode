class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        q=[]
        graph={i:[] for i in range(n)}
        degree=[0]*n
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
            degree[i]+=1
            degree[j]+=1
        for i,j in enumerate(degree):
            if j==1:
                q.append(i)
        rn=n
        while rn>2:
            nl=len(q)
            rn-=nl
            for i in range(nl):
                cl=q.pop(0)
                for neigh in graph[cl]:
                    degree[neigh]-=1
                    if degree[neigh]==1:
                        q.append(neigh)
        return q