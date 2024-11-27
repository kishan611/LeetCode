class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        d=[[i+1] for i in range(n)]
        res=[]
        def bfs():
            q=deque()
            visit=set()
            q.append((0,0))
            while q:
                curr,l=q.popleft()
                if curr==n-1:
                    return l
                for des in d[curr]:
                    if des not in visit:
                        visit.add(des)
                        q.append((des,l+1))
        for i,j in queries:
            d[i].append(j)
            res.append(bfs())
        return res