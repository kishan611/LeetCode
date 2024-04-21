class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if not edges or source==destination:
            return True
        d={i:[] for i in range(n)}
        for i in edges:
            d[i[0]].append(i[1])
            d[i[1]].append(i[0])
        s=d[source]
        visited={source}
        while s:
            x=s.pop()
            if x==destination:
                return True
            if x not in visited:
                visited.add(x)
                for i in d[x]:
                    if i not in visited:
                        s.append(i)
        return False
                        
                    