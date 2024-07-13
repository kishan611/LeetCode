class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n=len(positions)
        data=[[positions[i],healths[i],directions[i],i] for i in range(n)]
        data.sort()
        s=[]
        for i in data:
            if i[2]=="R" or not s or s[-1][2]=="L":
                s.append(i)
                continue
            status=1
            while s and s[-1][2]=="R" and status:
                lh=s[-1][1]
                if lh<i[1]:
                    s.pop()
                    i[1]-=1
                elif lh>i[1]:
                    s[-1][1]-=1
                    status=0
                else:
                    s.pop()
                    status=0
            if status:
                s.append(i)
        return [i[1] for i in sorted(s,key=lambda x:x[3])]
    
        
        