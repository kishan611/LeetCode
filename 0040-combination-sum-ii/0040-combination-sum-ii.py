class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        temp=[]
        n=len(candidates)
        candidates.sort()
        def helper(idx,target):
            if target==0:
                res.append(temp[::])
                return 
            for i in range(idx,n):
                if i>idx and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>target:
                    break
                temp.append(candidates[i])
                helper(i+1,target-candidates[i])
                temp.pop()
        helper(0,target)
        return res
                