class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        v=set()
        def dfs(node):
            s=[node]
            while s:
                c=s.pop()
                if c not in v:
                    v.add(c)
                    for i in g[c]:
                        if i not in v:
                            s.append(i)
        g={}
        for i,j in stones:
            if i not in g:
                g[i]=[]
            if ~j not in g:
                g[~j]=[]
            g[i].append(~j)
            g[~j].append(i)
        
        res=0
        for i,j in stones:
            if i not in v:
                dfs(i)
                res+=1
        return len(stones)-res

