class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        for i in range(len(candidates)):
            x=bin(candidates[i])[2:][::-1]
            x+="0"*(24-len(x))
            candidates[i]=x
        res=0
        for i in range(24):
            count=0
            for j in candidates:
                if j[i]=="1":
                    count+=1
            res=max(count,res)
        return res