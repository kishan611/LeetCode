class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x=y=d=0
        l=[(0,1),(1,0),(0,-1),(-1,0)]
        obstacles=set(map(tuple,obstacles))
        res=0
        for i in commands:
            if i==-1:
                d=(d+1)%4
            elif i==-2:
                d=(d-1)%4
            else:
                for j in range(i):
                    a,b=x+l[d][0],y+l[d][1]
                    if (a,b) in obstacles:
                        break
                    x,y=a,b
                res=max(res,x**2+y**2)
        return res