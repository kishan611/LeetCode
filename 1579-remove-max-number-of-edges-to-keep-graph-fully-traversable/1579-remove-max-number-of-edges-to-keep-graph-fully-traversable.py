class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        class UnionFind:
            def __init__(self,n):
                self.representative=list(range(n+1))
                self.component_size=[1]*(n+1)
                self.components=n
            def find(self,x):
                if self.representative[x]==x:
                    return x
                self.representative[x]=self.find(self.representative[x])
                return self.representative[x]
            def union(self,x,y):
                x=self.find(x)
                y=self.find(y)
                if x==y:
                    return 0
                if self.component_size[x]>self.component_size[y]:
                    self.component_size[x]+=self.component_size[y]
                    self.representative[y]=x
                else:
                    self.component_size[y]+=self.component_size[x]
                    self.representative[x]=y
                self.components-=1
                return 1
            def is_connected(self):
                return self.components==1
        a=UnionFind(n)
        b=UnionFind(n)
        er=0
        for e in edges:
            if e[0]==3:
                er+=(a.union(e[1],e[2]) | b.union(e[1],e[2]))
        for e in edges:
            if e[0]==2:
                er+=b.union(e[1],e[2])
            elif e[0]==1:
                er+=a.union(e[1],e[2])
        if a.is_connected() and b.is_connected():
            return len(edges)-er
        return -1
        