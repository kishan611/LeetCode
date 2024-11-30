class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)
        inOutDeg = defaultdict(int)
        for s, e in pairs:
            g[s].append(e)
            inOutDeg[s] += 1
            inOutDeg[e] -= 1
        startNode = pairs[0][0] 
        for n in inOutDeg:
            if inOutDeg[n] == 1:
                startNode = n
                break
        p = []
        def dfs(curr):
            while g[curr]:
                nn = g[curr].pop()
                dfs(nn)
                p.append((curr, nn))

        dfs(startNode)
        return p[::-1]