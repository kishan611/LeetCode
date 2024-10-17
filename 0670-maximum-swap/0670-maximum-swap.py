class Solution:
    def maximumSwap(self, num: int) -> int:
        num=list(str(num))
        n=len(num)
        for i in range(n):
            s=[]
            for j in range(i+1,n):
                if num[j]>num[i]:
                    s.append((num[j],j))
            if s:
                x,idx=max(s)
                num[i],num[idx]=num[idx],num[i]
                break
        return int("".join(num))

        