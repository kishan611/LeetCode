class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=[0]*26
        for i in tasks:
            count[ord(i)-65]+=1
        count.sort()
        curr=count[25]-1
        idle=curr*n
        for i in range(24,-1,-1):
            idle-=min(count[i],curr)
        return len(tasks)+idle if idle>=0 else len(tasks)
            
            