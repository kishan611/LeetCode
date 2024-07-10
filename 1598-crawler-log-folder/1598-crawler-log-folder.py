class Solution:
    def minOperations(self, logs: List[str]) -> int:
        x=0
        for i in logs:
            if i=="../":
                if x:
                    x-=1
            elif i=="./":
                continue
            else:
                x+=1
        return x
        