class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d={}
        for i in paths:
            d[i[0]]=i[1]
        x=paths[0][0]
        while True:
            if x in d:
                x=d[x]
            else:
                return x