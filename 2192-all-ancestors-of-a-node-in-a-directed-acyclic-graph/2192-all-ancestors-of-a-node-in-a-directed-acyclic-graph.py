class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        inc=[0]*n
        g=defaultdict(list)
        a=[set() for _ in range(n)]
        for i,j in edges:
            g[i].append(j)
            a[j].add(i)
            inc[j]+=1
        q=[]
        for i in range(n):
            if not a[i]:
                q.append(i)
        while q:
            node=q.pop()
            for adj in g[node]:
                a[adj].update(a[node])
                inc[adj]-=1
                if not inc[adj]:
                    q.append(adj)
        return [sorted(i) for i in a]
        