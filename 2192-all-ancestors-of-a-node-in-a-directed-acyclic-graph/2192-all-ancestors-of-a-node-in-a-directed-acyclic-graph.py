class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        res=[set() for i in range(n)]
        for i,j in edges:
            res[j].add(i)
        for i in range(n):
            s=res[i].copy()
            while s:
                x=s.pop()
                for j in res[x]:
                    if j not in res[i]:
                        res[i].add(j)
                        s.add(j)
        return [sorted(list(i)) for i in res]
                