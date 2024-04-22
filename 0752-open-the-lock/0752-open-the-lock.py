class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends=set(deadends)
        if "0000" in deadends:
            return -1
        v={"0000"}
        q=[('0000',0)]
        while q:
            cs,m=q.pop(0)
            if cs==target:
                return m
            for i in range(4):
                for j in [-1,1]:
                    d=str((int(cs[i])+j)%10)
                    nc=cs[:i]+d+cs[i+1:]
                    if nc not in v and nc not in deadends:
                        q.append((nc,m+1))
                        v.add(nc)
        return -1
        